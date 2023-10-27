# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.localrolesoverview


class CollectiveLocalrolesoverviewviewLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.localrolesoverview)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.localrolesoverview:default")


COLLECTIVE_LOCALROLESOVERVIEW_FIXTURE = CollectiveLocalrolesoverviewviewLayer()


COLLECTIVE_LOCALROLESOVERVIEW_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_LOCALROLESOVERVIEW_FIXTURE,),
    name="CollectiveLocalrolesoverviewviewLayer:IntegrationTesting",
)


COLLECTIVE_LOCALROLESOVERVIEW_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_LOCALROLESOVERVIEW_FIXTURE,),
    name="CollectiveLocalrolesoverviewviewLayer:FunctionalTesting",
)


COLLECTIVE_LOCALROLESOVERVIEW_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_LOCALROLESOVERVIEW_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="CollectiveLocalrolesoverviewviewLayer:AcceptanceTesting",
)
