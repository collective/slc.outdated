from Products.CMFCore.utils import getToolByName
from slc.outdated.tests.base import INTEGRATION_TESTING

import unittest2 as unittest


class TestInstall(unittest.TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_installed(self):
        self.failUnless(self.installer.isProductInstalled('slc.outdated'))

    def test_uninstall(self):
        self.installer.uninstallProducts(['slc.outdated'])
        self.failIf(self.installer.isProductInstalled('slc.outdated'))

    def test_action_registered(self):
        portal_actions = getToolByName(self.portal, 'portal_actions')
        self.assertIn('toggle_outdated', portal_actions.object_buttons.keys())

    def test_index_added(self):
        catalog = getToolByName(self.portal, 'portal_catalog')
        self.assertIn('outdated', catalog.indexes())


def test_suite():
    """This sets up a test suite that actually runs the tests in the class(es)
    above.
    """
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
