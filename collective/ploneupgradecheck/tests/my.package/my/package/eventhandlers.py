from zope.app.component.hooks import setSite, getSite


def object_removed(obj, event):
    getSite()
