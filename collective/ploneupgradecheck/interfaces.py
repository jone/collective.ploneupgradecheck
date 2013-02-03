from zope.interface import Interface



class IFileRegistry(Interface):
    """The ``IFileRegistry`` utility handles searching files by extension recursively.
    """

    def find_files(extensions=None):
        """Returns a list of file paths with one of the passed ``extensions``.
        """

    def load(path=None):
        """Loads the file registry.
        """

    def clear():
        """Clears the file registry.
        """

    def get_basedir():
        """Returns the base directory with which the registry was loaded or ``None`` if it
        was not loaded yet.
        """

    def grep(regexp, extensions=None):
        """Greps all files with the passed ``extensions`` for a ``regexp`` (compiled) per
        line.
        """
