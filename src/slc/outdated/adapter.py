from Products.ZCatalog.interfaces import IZCatalog
from plone.indexer.interfaces import IIndexer
from zope.annotation.interfaces import IAnnotatable, IAnnotations
from zope.component import adapter
from zope.interface import implementer

ANNOTATION_KEY = 'slc.outdated'


class Outdated(object):
    """Descriptor object to retrieve and set the outdated flag
    """
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if IAnnotatable.providedBy(obj.context):
            return IAnnotations(obj.context).get(ANNOTATION_KEY, False)
        return False

    def __set__(self, obj, val):
        if obj is None:
            raise AttributeError("Can't set attribute")
        if IAnnotatable.providedBy(obj.context):
            IAnnotations(obj.context)[ANNOTATION_KEY] = val


@implementer(IIndexer)
@adapter(IAnnotatable, IZCatalog)
class OutdatedIndexer(object):
    """Index the annotated outdated flag
    """

    outdated = Outdated()

    def __init__(self, context, catalog):
        self.context = context
        self.catalog = catalog

    def __call__(self):
        return self.outdated
