from plone import api
from Products.CMFCore.utils import getToolByName
from slc.outdated.tests.base import INTEGRATION_TESTING
try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None

import unittest


class TestInstall(unittest.TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer is not None:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_installed(self):
        self.assertTrue(self.installer.isProductInstalled('slc.outdated'))

    @unittest.skip("FIXME, low priority")
    def test_uninstall(self):
        with api.env.adopt_roles(["Manager"]):
            self.installer.uninstall_product('slc.outdated')
        self.assertFalse(self.installer.is_product_installed('slc.outdated'))

    def test_action_registered(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        self.assertIn('toggle_outdated', portal_actions.object_buttons)

    def test_index_added(self):
        catalog = getToolByName(self.portal, 'portal_catalog')
        self.assertIn('outdated', catalog.indexes())


def test_suite():
    """This sets up a test suite that actually runs the tests in the class(es)
    above.
    """
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
