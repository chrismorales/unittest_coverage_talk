##################################################
Unit Test Coverage Tool, Your Friendly Illusionist
##################################################

Building Presentation
=====================

Installing Prerequisites
------------------------

.. code-block::

    1. git clone git@github.com:chrismorales/unittest_coverage_talk.git
    2. cd unittest_coverage_talk
    3. virtualenv.py _env27 --prompt="(unittest_coverage_talk)"
    4. source _env27/bin/activate
    5. pip install --editable .

Building Slides
---------------

.. code-block::

    rst2html5 --jquery --reveal-js --pretty-print-code docs/index.rst > output/reveal.html




The Illusions of Coverage
=========================

Wrote unit tests for your entire module?
