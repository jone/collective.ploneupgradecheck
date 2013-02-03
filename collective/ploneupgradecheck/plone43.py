from collective.ploneupgradecheck import initialize
from collective.ploneupgradecheck.checker import Checker
import os

CONFIG = {
    'moved_imports': [

        # zope.app.component.hooks
        {'from': 'zope.app.component.hooks.getSite',
         'to': 'zope.component.hooks.getSite',
         'minimum': 'Plone 4.0'},

        {'from': 'zope.app.component.hooks.setSite',
         'to': 'zope.component.hooks.setSite',
         'minimum': 'Plone 4.0'},

        # zope.container
        {'from': 'zope.app.container.interfaces.INameChooser',
         'to': 'zope.container.interfaces.INameChooser',
         'minimum': 'Plone 4.1'},

        {'from': 'zope.app.container.interfaces.IOrderedContainer',
         'to': 'zope.container.interfaces.IOrderedContainer'},

        {'from': 'zope.app.container.interfaces.IAdding',
         'to': 'zope.browser.interfaces.IAdding',
         'minimum': 'Plone 4.1'},

        {'from': 'zope.app.container.contains',
         'to': 'zope.container.contains',
         'minimum': 'Plone 4.0'},

        {'from': 'zope.app.container.contained',
         'to': 'zope.container.contained',
         'minimum': 'Plone 4.0'},

        # zope.app.form
        {'from': 'zope.app.form.interfaces.WidgetInputError',
         'to': 'zope.formlib.interfaces.WidgetInputError',
         'minimum': 'Plone 4.1'},

        # zope.app.pagetemplate
        {'from': 'zope.app.pagetemplate.viewpagetemplatefile.ViewPageTemplateFile',
         'to': 'zope.browserpage.viewpagetemplatefile.ViewPageTemplateFile',
         'minimum': 'Plone 4.1'},


        ],

    'removed': [
        'elementtree',
        'Products.kupu',
        'plone.app.kss',
        'zope.app.cache',
        'zope.app.component',
        'zope.app.container',
        'zope.app.pagetemplate',
        'zope.app.publisher',
        'zope.copypastemove',
        'zope.dublincore'
        'zope.hookable',
        ]

    }


# zope.app.container events
for name in ('IObjectMovedEvent', 'IObjectAddedEvent',
             'IObjectRemovedEvent', 'IContainerModifiedEvent'):

    CONFIG['moved_imports'].append({
            'from': 'zope.app.container.interfaces.%s' % name,
            'to': 'zope.lifecycleevent.interfaces.%s' % name,
            'minimum': 'Plone 4.1'})


def check():
    initialize(os.getcwd())
    Checker(CONFIG)()
