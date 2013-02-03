class ColorString(str):
    """A colored string representation with fixed length and able to
    concatenate itself with other color strings.
    """

    COLORS = {
        'red'           : '\033[0;31m%s\033[00m',
        'green'         : '\033[0;32m%s\033[00m',
        'yellow'        : '\033[0;33m%s\033[00m',
        'blue'          : '\033[0;34m%s\033[00m',
        'purple'        : '\033[0;35m%s\033[00m',
        'magenta'       : '\033[0;36m%s\033[00m',
        'red_bold'      : '\033[1;31m%s\033[00m',
        'green_bold'    : '\033[1;32m%s\033[00m',
        'yellow_bold'   : '\033[1;33m%s\033[00m',
        'yellow_bold'   : '\033[1;33m%s\033[00m',
        'blue_bold'     : '\033[1;34m%s\033[00m',
        'purple_bold'   : '\033[1;35m%s\033[00m',
        'magenta_bold'  : '\033[1;36m%s\033[00m',
        'none'          : '%s',
        }


    def __new__(cls, value, colorname):
        colorized = ColorString.COLORS[colorname] % value
        self = str.__new__(cls, colorized)
        self.value = value
        return self

    def __len__(self):
        return len(self.value)

    def ljust(self, width):
        s = str(self)
        if width - len(self) > 0:
            s += ' ' * (width - len(self))
        return s

    def __add__(self, other):
        if isinstance(other, ColorString):
            value = self.value + other.value
        else:
            value = self.value + str(other)

        newstr = str( self ) + str( other )
        newobj = ColorString(newstr, 'none')
        newobj.value = value
        return newobj
