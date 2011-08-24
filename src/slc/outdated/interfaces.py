"""Define interfaces for your add-on.
"""

import zope.interface
from zope.component.interfaces import IObjectEvent


class IAddOnInstalled(zope.interface.Interface):
    """A layer specific for this add-on product.

    This interface is referred in browserlayers.xml.

    All views and viewlets register against this layer will appear on your
    Plone site only when the add-on installer has been run.
    """


class IObjectOutdatedToggleEvent(IObjectEvent):
    """An event that gets fired when the outdated status of an item is changed
    """

    object = zope.interface.Attribute("The object being handled.")
    status = zope.interface.Attribute("The new outdated status.")
