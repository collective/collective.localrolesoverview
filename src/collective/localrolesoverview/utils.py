from collective.localrolesoverview import _
from plone import api
from Products.CMFCore.utils import getToolByName

AUTH_GROUP = "AuthenticatedUsers"
STICKY = (AUTH_GROUP,)


def _local_roles_settings(context):
    info = []
    acl_users = getToolByName(context, "acl_users")
    portal_groups = getToolByName(context, "portal_groups")

    local_roles = acl_users._getLocalRolesForDisplay(context)
    items = {}
    for name, roles, rtype, rid in local_roles:
        if rid in items:
            items[rid]["local"] = roles
        else:
            items[rid] = dict(
                id=rid,
                name=name,
                type=rtype,
                sitewide=[],
                acquired=[],
                local=roles,
            )

    dec_users = [
        (a["id"] not in STICKY, a["type"], a["name"], a)
        for a in items.values()
    ]
    dec_users.sort()
    for d in dec_users:
        item = d[-1]
        name = item["name"]
        rid = item["id"]
        login = rid
        global_roles = set()

        if item["type"] == "user":
            member = acl_users.getUserById(rid)
            if member is not None:
                name = (
                    member.getProperty("fullname") or member.getUserName() or name
                )
                global_roles = set(member.getRoles())
                login = member.getUserName()
        elif item["type"] == "group":
            g = portal_groups.getGroupById(rid)
            name = g.getGroupTitleOrName()
            login = None
            global_roles = set(g.getRoles())

            # This isn't a proper group, so it needs special treatment :(
            if rid == AUTH_GROUP:
                name = _("Logged-in users")

        info_item = dict(
            id=item["id"],
            type=item["type"],
            title=name,
            local_roles=item['local'],
            global_roles=global_roles,
        )
        if login != name:
            info_item["login"] = login
        if info_item["local_roles"] or info_item["global_roles"]:
            info.append(info_item)
    return info


def build_local_roles_map(context):
    lrmap = {}
    brains = api.content.find(context=context, is_folderish=True)
    for brain in brains:
        obj = brain.getObject()
        rolemaps = _local_roles_settings(obj)
        for rolemap in rolemaps:
            if rolemap["id"] not in lrmap:
                lrmap[rolemap["id"]] = {
                    "paths": [],
                    "title": rolemap["title"],
                    "type": rolemap["type"],
                }
            if obj.absolute_url_path() not in lrmap[rolemap["id"]]:
                lrmap[rolemap["id"]][obj.absolute_url_path()] = {}
            lrmap[rolemap["id"]]["paths"].append(obj.absolute_url_path())
            lrmap[rolemap["id"]][obj.absolute_url_path()] = {
                "url": obj.absolute_url(),
                "roles": [r for r in rolemap["local_roles"] if r],
            }
    return lrmap

