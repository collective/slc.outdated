from slc.outdated.interfaces import IObjectOutdatedToggleEvent
from zope.interface import implements


class ObjectOutdatedToggleEvent(object):
    """Sent before an object is translated."""
    implements(IObjectOutdatedToggleEvent)

    def __init__(self, context, status):
        self.object = context
        self.status = status
