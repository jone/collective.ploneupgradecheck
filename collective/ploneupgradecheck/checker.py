from collective.ploneupgradecheck.interfaces import IImportRegistry
from collective.ploneupgradecheck.colorstring import ColorString
from zope.component import getUtility



class Checker(object):

    def __init__(self, config):
        self._files_by_extension = None
        self.config = config

    def __call__(self):
        self.check_moved_imports()
        self.check_removed()

    def error(self, path, msg, details=None):
        print ColorString(path, 'blue')
        print '   ', msg
        if details:
            print '   ', details
        print ''

    def check_moved_imports(self):
        for item in self.config.get('moved_imports', []):
            self._check_import(item)

    def _check_import(self, item):
        registry = getUtility(IImportRegistry)

        for path, dottedname in registry.get_imports(item.get('from')):
            self.error(
                path,
                'Import %s should be changed' % dottedname,
                '%s was moved to %s%s' % (
                    ColorString(item.get('from'), 'red'),
                    ColorString(item.get('to'), 'green'),
                    item.get('minimum') and ' (%s)' % item.get('minimum') or ''))

    def check_removed(self):
        registry = getUtility(IImportRegistry)

        for removed in self.config.get('removed', []):
            for path, dottedname in registry.get_imports(removed):
                self.error(
                    path,
                    'Package %s is no longer part of the Plone core' % (
                        ColorString(removed, 'red')))
