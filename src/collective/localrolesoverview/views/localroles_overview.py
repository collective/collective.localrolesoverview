# -*- coding: utf-8 -*-

# from collective.localrolesoverview import _
from ..utils import build_local_roles_map
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ILocalrolesOverview(Interface):
    """Marker Interface for ILocalrolesOverview"""


@implementer(ILocalrolesOverview)
class LocalrolesOverview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('permissions_overview.pt')

    def __call__(self):
        # Implement your own actions:
        self.lrmap = build_local_roles_map(self.context)
        return self.index()

    @property
    def principal_ids_sorted(self):
        principals = []
        for pid in self.lrmap.keys():
            principals.append(pid)
        return sorted(principals)


