from collective.ploneupgradecheck.imports import ImportRegistry
from collective.ploneupgradecheck.interfaces import IFileRegistry
from collective.ploneupgradecheck.interfaces import IImportRegistry
from collective.ploneupgradecheck.testing import ZCML_LAYER
from collective.ploneupgradecheck.tests.utils import relative_path
from unittest2 import TestCase
from zope.component import getUtility
from zope.interface.verify import verifyClass


def make_paths_relative(basedir, result):
    for path, dottedname in result:
        path = relative_path(basedir, path)
        yield path, dottedname


def filter_results_by_path(path, results):
    basedir = getUtility(IFileRegistry).get_basedir()

    for result_path, dottedname in make_paths_relative(basedir, results):
        if result_path == path:
            yield (result_path, dottedname)


class TestImportRegistry(TestCase):

    layer = ZCML_LAYER

    def test_implements_interface(self):
        self.assertTrue(IImportRegistry.implementedBy(ImportRegistry))
        verifyClass(IImportRegistry, ImportRegistry)

    def test_utility_registered(self):
        getUtility(IImportRegistry)

    def test_python_imports_detected(self):

        registry = getUtility(IImportRegistry)
        results = registry.get_imports('zope.app.component.hooks')
        results = list(filter_results_by_path('my/package/eventhandlers.py', results))

        self.assertEqual(len(results), 1)
        path, dottedname = results[0]
        self.assertEqual(path, 'my/package/eventhandlers.py')
        self.assertEqual(dottedname, 'zope.app.component.hooks.getSite')
