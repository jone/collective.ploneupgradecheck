from collective.ploneupgradecheck.files import FileRegistry
from collective.ploneupgradecheck.interfaces import IFileRegistry
from collective.ploneupgradecheck.testing import ZCML_LAYER
from collective.ploneupgradecheck.tests.utils import relative_path
from collective.ploneupgradecheck.tests.utils import relative_paths
from unittest2 import TestCase
from zope.component import getUtility
from zope.interface.verify import verifyClass
import os.path
import re


class TestFileRegistry(TestCase):

    layer = ZCML_LAYER

    def test_implements_interface(self):
        self.assertTrue(IFileRegistry.implementedBy(FileRegistry))
        verifyClass(IFileRegistry, FileRegistry)

    def test_utility_registered(self):
        getUtility(IFileRegistry)

    def test_get_basedir(self):
        registry = getUtility(IFileRegistry)
        self.assertEqual(registry.get_basedir(),
                         os.path.join(os.path.dirname(__file__), 'my.package'))

    def test_find_files(self):
        registry = getUtility(IFileRegistry)

        py_files = relative_paths(registry.get_basedir(), registry.find_files(['py']))
        self.assertIn('my/package/eventhandlers.py', py_files)
        self.assertNotIn('my/package/configure.zcml', py_files)

        zcml_files = relative_paths(registry.get_basedir(), registry.find_files(['zcml']))
        self.assertNotIn('my/package/eventhandlers.py', zcml_files)
        self.assertIn('my/package/configure.zcml', zcml_files)

        both_files = relative_paths(registry.get_basedir(), registry.find_files(['zcml', 'py']))
        self.assertIn('my/package/eventhandlers.py', both_files)
        self.assertIn('my/package/configure.zcml', both_files)

    def test_clear_and_load(self):
        basedir = getUtility(IFileRegistry).get_basedir()

        # use a fresh registry, so that we dont destroy later tests on failure
        registry = FileRegistry()

        self.assertFalse(registry.get_basedir())
        self.assertFalse(registry.find_files())

        registry.load(basedir)

        self.assertTrue(registry.get_basedir())
        self.assertTrue(registry.find_files())

        registry.clear()

        self.assertFalse(registry.get_basedir())
        self.assertFalse(registry.find_files())

    def test_grep(self):
        regexp = re.compile('def ([a-zA-Z0-9_]*)(\(.*?\):)')

        registry = getUtility(IFileRegistry)
        matches = registry.grep(regexp, extensions=['py'])

        self.assertEqual(len(matches), 1)
        match = matches[0]

        path = relative_path(registry.get_basedir(), match.get('path'))
        self.assertEqual(path, 'my/package/eventhandlers.py')

        self.assertEqual(match.get('groups'), ('object_removed', '(obj, event):'))

    def test_ignored_files_not_in_registry(self):
        registry = getUtility(IFileRegistry)

        self.assertNotIn('foo', registry._files_by_extension)
