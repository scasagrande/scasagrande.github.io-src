Software Projects
#################

:slug: software
:menulabel: Software
:url: software


Instrument Kit
--------------

.. image:: https://img.shields.io/travis/Galvant/InstrumentKit.svg?maxAge=2592000
    :target: https://travis-ci.org/Galvant/InstrumentKit
    :alt: Travis-CI build status

.. image:: https://img.shields.io/coveralls/Galvant/InstrumentKit/dev.svg?maxAge=2592000
    :target: https://coveralls.io/r/Galvant/InstrumentKit?branch=dev
    :alt: Coveralls code coverage

.. image:: https://readthedocs.org/projects/instrumentkit/badge/?version=latest
    :target: https://readthedocs.org/projects/instrumentkit/?badge=latest
    :alt: Documentation

**Language**: Python

**Source Code**: `github.com/Galvant/InstrumentKit <https://www.github.com/Galvant/InstrumentKit>`_

InstrumentKit is an open source Python library designed to help the
end-user get straight into communicating with their test and measurement equipment via a PC.
InstrumentKit aims to accomplish this by providing a connection- and
vendor-agnostic API. Users can freely swap between a variety of
connection types (ethernet, gpib, serial, usb) without impacting their
code. Since the API is consistent across similar instruments, a user
can, for example, upgrade from their 1980's multimeter using GPIB to a
modern Keysight 34461a using ethernet with only a single line change.
