from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile


class SlcOutdated(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import slc.outdated
        self.loadZCML('configure.zcml', package=slc.outdated)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'slc.outdated:default')


SLC_OUTDATED_FIXTURE = SlcOutdated()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(SLC_OUTDATED_FIXTURE,),
    name="SlcOutdated:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SLC_OUTDATED_FIXTURE,),
    name="SlcOutdated:Functional")
