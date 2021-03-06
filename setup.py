import os
from setuptools import setup, find_packages


version = '1.0.dev0'


tests_require = [
    'unittest2',
    'plone.testing',
    ]


extras_require = {
    'tests': tests_require}


setup(name='collective.ploneupgradecheck',
      version=version,
      description='Simple check for upgrading a plone addon to a newer '
      'plone version.',

      long_description=open('README.rst').read() + '\n' + \
          open(os.path.join('docs', 'HISTORY.txt')).read(),

      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],

      keywords='plone upgrade check',
      author='Jonas Baumann',
      author_email='mailto:jone@jone.ch',
      url='https://github.com/jone/collective.ploneupgradecheck',

      license='Beerware42',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', ],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',
        'zope.interface',
        'zope.component',
        'zope.configuration',
        ],

      tests_require=tests_require,
      extras_require=extras_require,

      entry_points = {
        'console_scripts': [
            'plone-4.3-check = collective.ploneupgradecheck.plone43:check',
            ],
        })
