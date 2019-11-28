import unittest
from plone import api
from plone.app.testing import helpers, SITE_OWNER_NAME
from slc.outdated.tests.base import INTEGRATION_TESTING
from slc.outdated.utils import is_outdated


class TestIndexer(unittest.TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        helpers.login(self.layer["app"], SITE_OWNER_NAME)
        self.testfile = api.content.create(
            self.portal, type="File", title="A Test File"
        )

    def test_is_outdated(self):
        toggleview = self.testfile.restrictedTraverse("object_toggle_outdated")
        self.assertFalse(is_outdated(self.testfile))
        toggleview()
        self.assertTrue(is_outdated(self.testfile))
