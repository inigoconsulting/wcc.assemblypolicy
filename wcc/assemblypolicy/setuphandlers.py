from plone.app.controlpanel.filter import IFilterSchema

def setupVarious(context):
    if context.readDataFile('wcc.assemblypolicy.marker.txt') is None:
        # Not your add-on
        return

    portal = context.getSite()
    allow_embed_tags(portal)

def allow_embed_tags(portal):
    filtering = IFilterSchema(portal)
    nasty_tags = filtering.nasty_tags
    for t in ['embed','param','iframe','object','script']:
        if t in nasty_tags:
            nasty_tags.remove(t)
    filtering.nasty_tags = nasty_tags
    custom_tags = filtering.custom_tags
    for t in ['iframe']:
        if t not in custom_tags:
            custom_tags.append(t)
    filtering.custom_tags = custom_tags
