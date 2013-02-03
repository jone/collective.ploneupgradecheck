from collective.ploneupgradecheck.interfaces import IFileRegistry
from zope.component import getUtility
from zope.configuration import xmlconfig


def initialize(path):
    import collective.ploneupgradecheck
    xmlconfig.file('configure.zcml', collective.ploneupgradecheck)

    getUtility(IFileRegistry).load(path)
