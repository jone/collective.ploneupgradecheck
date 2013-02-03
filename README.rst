collective.ploneupgradecheck
============================

``collective.ploneupgradecheck`` helps you upgrade your plone addon to a newer version.
It installs simple console scripts doing superficial checks of your code and reports
things that need to be changed, such as imports.


Compatibility
-------------

- Upgrade checks for Plone `4.3`.


Usage
-----

Check out the repository and run the included buildout:

.. code:: bash

    $ git clone https://github.com/jone/collective.ploneupgradecheck.git
    $ cd collective.ploneupgradecheck
    $ python bootstrap.py
    $ bin/buildout

This generates a ``bin/plone-4.3-check`` script.
Run the script in any directory with code to check.


Links
-----

- Main github project repository: https://github.com/jone/collective.ploneupgradecheck
- Issue tracker: https://github.com/jone/collective.ploneupgradecheck/issues


Contributions
-------------

Contributions are welcome!
Fork the repository on github, change your code and make a pull request.


License
-------

"THE BEER-WARE LICENSE" (Revision 42):

jone_ wrote this script. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return.
