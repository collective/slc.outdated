import unittest
import mock

from plone import api
from plone.app.testing import helpers, SITE_OWNER_NAME
from zope.annotation.interfaces import IAnnotations
from zope.interface import Interface

from slc.outdated.adapter import ANNOTATION_KEY
from slc.outdated.interfaces import IObjectOutdatedToggleEvent
from slc.outdated.tests.base import INTEGRATION_TESTING


class TestToggle(unittest.TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        helpers.login(self.layer['app'], SITE_OWNER_NAME)
        self.testfile = api.content.create(
            self.portal,
            type='File',
            title='A Test File',
        )
        self.testpage = api.content.create(
            self.portal,
            type='Document',
            title='A Test Page',
        )

    def test_toggle_sets_outdated(self):
        """Calling the toggle view on a non-outdated object sets it to
        outdated."""
        helpers.login(self.layer['app'], SITE_OWNER_NAME)
        toggleview = self.testpage.restrictedTraverse('object_toggle_outdated')
        self.assertFalse(toggleview.outdated)
        toggleview()
        self.assertTrue(toggleview.outdated)

    def test_event_fired(self):
        """Calling the toggle view triggers a custom event."""
        mock_handler = mock.Mock()
        sm = self.portal.getSiteManager()
        sm.registerHandler(
            mock_handler,
            required=[Interface, IObjectOutdatedToggleEvent],
        )

        helpers.login(self.layer['app'], SITE_OWNER_NAME)
        toggleview = self.testpage.restrictedTraverse('object_toggle_outdated')
        toggleview()
        mock_handler.assert_called_once()
        self.assertTrue(
            IObjectOutdatedToggleEvent.providedBy(mock_handler.call_args[0][1]),
        )

    def test_toggle_clears_outdated(self):
        """Calling the toggle view on an outdated object sets it to
        non-outdated."""
        helpers.login(self.layer['app'], SITE_OWNER_NAME)
        IAnnotations(self.testpage)[ANNOTATION_KEY] = True
        toggleview = self.testpage.restrictedTraverse('object_toggle_outdated')
        self.assertTrue(toggleview.outdated)
        toggleview()
        self.assertFalse(toggleview.outdated)

    def test_toggle_on_file_redirects_to_view(self):
        """Using the toggle view on a file should not redirect to download but
        to view."""
        helpers.login(self.layer['app'], SITE_OWNER_NAME)
        toggleview = self.testfile.restrictedTraverse('object_toggle_outdated')
        toggleview()
        self.assertTrue(
            toggleview.request.response.getHeader('Location').endswith('view'))

    def test_toggle_on_file_redirects_to_referer(self):
        """Using the toggle view on a file should redirect to the referer if it
        is set."""
        helpers.login(self.layer['app'], SITE_OWNER_NAME)
        self.portal.REQUEST.environ['REFERER'] = 'http://nohost/whereicamefrom'
        toggleview = self.testfile.restrictedTraverse('object_toggle_outdated')
        toggleview()
        self.assertEquals(
            toggleview.request.response.getHeader('Location'),
            'http://nohost/whereicamefrom')
