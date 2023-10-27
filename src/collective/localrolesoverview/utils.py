from plone import api


def build_local_roles_map(context):
    lrmap = {}
    brains = api.content.find(context=context, is_folderish=True)
    for brain in brains:
        obj = brain.getObject()
        sharing_view = api.content.get_view(name="sharing", context=obj)
        rolemaps = sharing_view.existing_role_settings()
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
                "roles": [r for r in rolemap["roles"] if r],
            }
    return lrmap

