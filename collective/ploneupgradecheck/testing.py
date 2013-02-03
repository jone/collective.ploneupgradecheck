from collective.ploneupgradecheck.interfaces import IFileRegistry
from collective.ploneupgradecheck.interfaces import IImportRegistry
from plone.testing import Layer
from plone.testing import zca
from zope.component import getUtility
from zope.configuration import xmlconfig
import os.path


class ZCMLLayer(Layer):

    def setUp(self):
        self['configurationContext'] = zca.stackConfigurationContext(
            self.get('configurationContext'))

        zca.pushGlobalRegistry()

        import collective.ploneupgradecheck
        self.load_zcml_file('configure.zcml', collective.ploneupgradecheck)

        self.my_package_path = os.path.join(os.path.dirname(__file__),
                                            'tests', 'my.package')

        file_registry = getUtility(IFileRegistry)
        file_registry.clear()
        file_registry.load(self.my_package_path)

        import_registry = getUtility(IImportRegistry)
        import_registry.clear()

    def tearDown(self):
        zca.popGlobalRegistry()
        del self['configurationContext']

    def load_zcml_file(self, filename, module):
        xmlconfig.file(filename, module,
                       context=self['configurationContext'])


ZCML_LAYER = ZCMLLayer()
