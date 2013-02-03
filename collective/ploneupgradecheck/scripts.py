from collective.ploneupgradecheck import initialize
from collective.ploneupgradecheck.checker import Checker
from collective.ploneupgradecheck.checker import plone43
import os


def plone43():
    initialize(os.getcwd())
    Checker(plone43)()
