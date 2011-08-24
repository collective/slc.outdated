from Products.CMFPlone.utils import getSiteEncoding
from Products.Five.browser import BrowserView
from Products.ZCatalog.interfaces import IZCatalog
from Products.statusmessages.interfaces import IStatusMessage
from plone.app.layout.viewlets.common import ViewletBase
from plone.indexer.interfaces import IIndexer
from slc.outdated.interfaces import IObjectOutdatedToggleEvent
from zope.annotation.interfaces import IAnnotatable
from zope.annotation.interfaces import IAnnotations
from zope.component import adapts
from zope.interface import implements
from zope.event import notify

ANNOTATION_KEY="slc.outdated"


class ObjectOutdatedToggleEvent(object):
    """Sent before an object is translated."""
    implements(IObjectOutdatedToggleEvent)

    def __init__(self, context, status):
        self.object = context
        self.status = status


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

    def __call__(self, value=None):
        msg = self.toggle(value)
        messages = IStatusMessage(self.request)
        messages.addStatusMessage(msg, type="info")
        self.request.response.redirect(self.context.absolute_url())

    def toggle(self, value=None):
        """ same as __call__ but without the redirect """
        if value is None:
            self.outdated = not self.outdated
        else:
            self.outdated = not not value
        if self.outdated:
            msg = u"Marked '%s' as outdated."
        else:
            msg = u"Removed outdated flag from '%s'."
        event = ObjectOutdatedToggleEvent(self.context, self.outdated)
        notify(event)
        name = self.context.title_or_id()
        if not isinstance(name, unicode):
            name = name.decode(getSiteEncoding(self.context))
        msg = msg % name
        self.context.reindexObject()
        return msg

class OutdatedViewlet(ViewletBase):
    """A viewlet that indicates that content is outdated
    """
    outdated = Outdated()

    def render(self):
        if not self.outdated:
            return ""
        return super(OutdatedViewlet, self).render()
