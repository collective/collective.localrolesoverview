.. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on PyPI or github. It is a comment.

.. image:: https://github.com/collective/collective.localrolesoverview/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/collective/collective.localrolesoverview/actions/workflows/plone-package.yml

.. image:: https://coveralls.io/repos/github/collective/collective.localrolesoverview/badge.svg?branch=main
    :target: https://coveralls.io/github/collective/collective.localrolesoverview?branch=main
    :alt: Coveralls

.. image:: https://codecov.io/gh/collective/collective.localrolesoverview/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/collective/collective.localrolesoverview

.. image:: https://img.shields.io/pypi/v/collective.localrolesoverview.svg
    :target: https://pypi.python.org/pypi/collective.localrolesoverview/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/collective.localrolesoverview.svg
    :target: https://pypi.python.org/pypi/collective.localrolesoverview
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/collective.localrolesoverview.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/collective.localrolesoverview.svg
    :target: https://pypi.python.org/pypi/collective.localrolesoverview/
    :alt: License


==============================
collective.localrolesoverview
==============================

Shows assigned local roles for all users, groups on all folderish content.

This packages provides a view called `@@localfolderroles-overview`, which you can call on any Plone context.

.. image:: https://github.com/collective/collective.localrolesoverview/raw/main/docs/screenshot.png

You can also ignore users `@@localfolderroles-overview?ignore_users=1`.

.. image:: https://github.com/collective/collective.localrolesoverview/raw/main/docs/screenshot-ignored-users.png


Installation
------------

Install collective.localrolesoverview by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.localrolesoverview


and then running ``bin/buildout``


Authors
-------

Provided by http://derico.de - Maik Derstappen (MrTango)


Contributors
------------

Put your name here, you deserve it!

- ?


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.localrolesoverview/issues
- Source Code: https://github.com/collective/collective.localrolesoverview


Support
-------

If you are having issues, please let us know.


License
-------

The project is licensed under the GPLv2.
