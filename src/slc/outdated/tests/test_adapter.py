import unittest
from plone import api
from plone.app.testing import helpers, SITE_OWNER_NAME
from slc.outdated.tests.base import INTEGRATION_TESTING


class TestIndexer(unittest.TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        helpers.login(self.layer["app"], SITE_OWNER_NAME)
        self.testfile = api.content.create(
            self.portal, type="File", title="A Test File"
        )

    def test_indexer(self):
        toggleview = self.testfile.restrictedTraverse("object_toggle_outdated")
        toggleview()
        catalog = api.portal.get_tool("portal_catalog")
        result = catalog(UID=api.content.get_uuid(self.testfile))
        self.assertTrue(result[0]["outdated"])
