from zope.app.component.hooks import getSite


def object_removed(obj, event):
    getSite()
