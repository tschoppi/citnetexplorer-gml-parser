CitNetExplorer GML Parser
=========================

Description
-----------

Citnetparser is a python module that provides a standalone executable for
converting the CitNetExplorer_ native format of two separate files into one file
following the standard Graph Modelling Language (GML_) specification, which is
known by many graph analysis programs.

Installing
----------

It is recommended to activate a virtual environment to install into.

Download the repository with ``git clone`` and install it with ``pip``:

::

    pip install .

The command automatically finds the setup file and then installs into the
virtual environment.

Usage
-----

The software can be then called from the command line while the virtual
environment is active:

::

    citnetparser ../path/to/publications.txt ../path/to/citations.txt output_file.gml


.. _CitNetExplorer: http://www.citnetexplorer.nl/
.. _GML: https://en.wikipedia.org/wiki/Graph_Modelling_Language
