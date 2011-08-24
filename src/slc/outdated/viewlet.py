from plone.app.layout.viewlets.common import ViewletBase
from slc.outdated import Outdated


class OutdatedViewlet(ViewletBase):
    """A viewlet that indicates that content is outdated
    """
    outdated = Outdated()

    def render(self):
        if not self.outdated:
            return ""
        return super(OutdatedViewlet, self).render()
