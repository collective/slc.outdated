from slc.outdated.interfaces import IObjectOutdatedToggleEvent
from zope.interface import implementer


@implementer(IObjectOutdatedToggleEvent)
class ObjectOutdatedToggleEvent(object):
    """Sent before an object's outdated state is changed."""

    def __init__(self, context, status):
        self.object = context
        self.status = status
