from Products.Five.browser import BrowserView
from Products.ZCatalog.interfaces import IZCatalog
from Products.statusmessages.interfaces import IStatusMessage
from plone.app.layout.viewlets.common import ViewletBase
from plone.indexer.interfaces import IIndexer
from zope.annotation.interfaces import IAnnotatable
from zope.annotation.interfaces import IAnnotations
from zope.component import adapts
from zope.interface import implements


ANNOTATION_KEY="slc.outdated"


class Outdated(object):
    """Descriptor object to retrieve and set the outdated flag
    """
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return IAnnotations(obj.context).get(ANNOTATION_KEY, False)

    def __set__(self, obj, val):
        if obj is None:
            raise AttributeError("Can't set attribute")
        IAnnotations(obj.context)[ANNOTATION_KEY] = val


class OutdatedIndexer(object):
    """Index the annotated outdated flag
    """
    implements(IIndexer)
    adapts(IAnnotatable, IZCatalog)

    outdated = Outdated()

    def __init__(self, context, catalog):
        self.context = context
        self.catalog = catalog

    def __call__(self):
        return self.outdated


class ToggleOutdated(BrowserView):
    """Toggle the outdated flag
    """
    outdated = Outdated()

    def __call__(self):
        self.outdated = not self.outdated
        if self.outdated:
            msg = u"Marked '%s' as outdated."
        else:
            msg = u"Removed outdated flag from '%s'."
        msg = msg % (self.context.title_or_id(),)
        messages = IStatusMessage(self.request)
        messages.addStatusMessage(msg, type="info")
        self.request.response.redirect(self.context.absolute_url())
        self.context.reindexObject(idxs=["outdated"])


class OutdatedViewlet(ViewletBase):
    """A viewlet that indicates that content is outdated
    """
    outdated = Outdated()

    def render(self):
        if not self.outdated:
            return ""
        return super(OutdatedViewlet, self).render()
