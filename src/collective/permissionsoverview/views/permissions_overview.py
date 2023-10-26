# -*- coding: utf-8 -*-

# from collective.permissionsoverview import _
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IPermissionsOverview(Interface):
    """Marker Interface for IPermissionsOverview"""


@implementer(IPermissionsOverview)
class PermissionsOverview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('permissions_overview.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
