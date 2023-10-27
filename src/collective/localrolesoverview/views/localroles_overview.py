# -*- coding: utf-8 -*-

# from collective.localrolesoverview import _
from ..utils import build_local_roles_map
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ILocalfolderrolesOverview(Interface):
    """Marker Interface for ILocalrolesOverview"""


@implementer(ILocalfolderrolesOverview)
class LocalfolderrolesOverview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('permissions_overview.pt')

    def __call__(self):
        # Implement your own actions:
        self.lrmap = build_local_roles_map(self.context)
        self.ignore_users = int(self.request.get("ignore_users", 0))
        return self.index()

    @property
    def principal_ids_sorted(self):
        principals = []
        for pid, principal in self.lrmap.items():
            if principal["type"] == "group" or not self.ignore_users:
                principals.append(pid)
        return sorted(principals)


