=======================
Pelican Plugin Template
=======================

.. image:: https://travis-ci.org/nebulousdog/thedropin.svg?branch=master
   :target: https://travis-ci.org/nebulousdog/thedropin
   :alt: travis-link
.. image:: https://codecov.io/gh/nebulousdog/thedropin/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/nebulousdog/thedropin
   :alt: codecov-link
.. image:: https://img.shields.io/pypi/v/thedropin.svg
   :target: https://pypi.org/project/thedropin/
   :alt: pypi-link

These are the bare minimum yet possibly over-explained steps for creating a Pelican plugin.

*****
Steps
*****

Please let us know in an `issue <https://github.com/nebulousdog/thedropin/issues>`_ if we forgot anything!

Copy Plugin Base
================

1. Fork `thedropin <https://github.com/nebulousdog/thedropin>`_.
2. Change all dir names and references to this project's name[1]_.

.. [1] Python project names are typically short and lower-cased. If you make a single-word project, congrats, you never have to worry about inconsistent casing between projects. If you absolutely must use spacing, use underscores for project names, directories, and filenames.

Dependencies
============

See instructions for installing `Pipenv <https://github.com/pypa/pipenv#installation>`_. Then run ``pipenv install --dev``.

Developing Your Plugin
======================

This is now where you get to get 🎨 creative! Good luck, have fun.

ETC
^^^

This is wading into dangerous territory to start recommending text-editor practices, but if you open your editor from inside the Pipenv shell, that may help your editor loading the proper environment-specific dependencies.

Tests
=====

1. ``pipenv run tests``

Linting
=======

1. ``pipenv run lints``

Sharing
=======

Two great ways to share your code with the community.

Pelican Plugins Community Repo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See `Contributing a plugin <https://github.com/getpelican/pelican-plugins/blob/master/Contributing.rst>`_ and `Using Git and Github <https://docs.getpelican.com/en/latest/contribute.html#using-git-and-github>`_ about adding a plugin to the ``pelican-plugins`` `repo <https://github.com/getpelican/pelican-plugins>`_.

Publishing to PyPI
^^^^^^^^^^^^^^^^^^

This is probably the hardest part, and is why I'd wager there are so few Pelican projects registered on PyPI[2]_. If you begin with the manual steps, I recommend migrating over to an automated way as soon as possible.

.. [2] This is based on the following three `classifier <https://pypi.org/classifiers/>`_ searches. At the time of writing these are the tallies, with possible overlap between them; `Framework :: Pelican <https://pypi.org/search/?q=&o=&c=Framework+%3A%3A+Pelican>`_ (20 projects) + `Framework :: Pelican :: Plugins <https://pypi.org/search/?c=Framework+%3A%3A+Pelican+%3A%3A+Plugins>`_ (12 projects) + `Framework :: Pelican :: Themes <https://pypi.org/search/?c=Framework+%3A%3A+Pelican+%3A%3A+Themes>`_ (5 projects) = 37.

First Time
""""""""""

Your first time uploading a project to PyPI requires registration via `Twine <https://github.com/pypa/twine>`_.

1. ``pipenv shell`` Enter your dev environment where ``twine`` will be accessible.
2. ``python setup.py sdist bdist_wheel`` Create a normal distribution.
3. `Register <https://pypi.org/account/register/>`_ on PyPI.

Optionally, you can do some checks on your distribution before attempting an official upload.

4. Also `register <https://pypi.org/account/register/>`_ on TestPyPI if you intend to test your distribution before making it official.
5. ``twine check dist/*`` Check the distribution you made in step 2.
6. ``twine upload --repository testpypi dist/*`` Run a test of the upload. Preview at https://test.pypi.org/project/thedropin.

Back to the official upload steps..

(TODO: going to rename the project before uploading to PyPI)

7. (TODO: left off here)

Automated Release to PyPI
"""""""""""""""""""""""""

(TODO: left off here)

After you've found your groove with this; Give yourself a pat on the back. Job well done.

You wont be needing Twine any more. Please feel free to uninstall with ``pipenv uninstall twine``.

**********
References
**********

* `Contributing and feedback guidelines <https://docs.getpelican.com/en/latest/contribute.html>`_
* `How to create plugins <https://docs.getpelican.com/en/latest/plugins.html#how-to-create-plugins>`_
* `Contributing a plugin <https://github.com/getpelican/pelican-plugins/blob/master/Contributing.rst>`_

*******
License
*******

MIT
