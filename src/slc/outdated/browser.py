from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from slc.outdated import Outdated, ObjectOutdatedToggleEvent
from zope.event import notify


class ToggleOutdated(BrowserView):
    """Toggle the outdated flag
    """
    outdated = Outdated()

    def __call__(self, value=None):
        msg = self.toggle(value)
        messages = IStatusMessage(self.request)
        messages.addStatusMessage(msg, type="info")
        redirect = self.request.get_header("referer") \
            or '/'.join([self.context.absolute_url(), 'view'])
        self.request.response.redirect(redirect)

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
        name = safe_unicode(self.context.title_or_id())
        msg = msg % name
        self.context.reindexObject()
        return msg
