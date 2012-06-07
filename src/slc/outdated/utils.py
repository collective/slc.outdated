from zope.component import queryMultiAdapter
from Products.CMFCore.utils import getToolByName
from plone.indexer.interfaces import IIndexer


def is_outdated(obj):
    """ Utility method to check if an object is outdated.
    """
    catalog = getToolByName(obj, 'portal_catalog')
    indexer = queryMultiAdapter((obj, catalog), IIndexer, name='outdated')
    return indexer()
