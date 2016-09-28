# -*- coding: utf-8 -*-

import os
from setuptools import find_packages
from setuptools import setup

# .......................................................................... #
# install requires
install_requires = [
    'rst2html5-tools',
    'nose',
    'coverage'
    ]

# .......................................................................... #
# development requires
develop_requires = [
    'ipython',
    ]

# .......................................................................... #
# testing requires
tests_requires = [
    ]


# .......................................................................... #
def main():

    # get content of README.rst and CHANGES.txt
    here = os.path.abspath(os.path.dirname(__file__))
    try:
        with open(os.path.join(here, 'README.rst')) as readme_file:
            README = readme_file.read()
        with open(os.path.join(here, 'CHANGES.rst')) as changes_file:
            CHANGES = changes_file.read()
    except IOError:
        README = CHANGES = ''

    # runs setuptools setup
    setup(name='unittest_coverage_talk',
          version='0.1dev',
          description='unittest_coverage_talk',
          long_description=README + '\n\n' + CHANGES,
          classifiers=[
              "Programming Language :: Python",
          ],
          author='',
          author_email='',
          url='',
          keywords='',
          packages=find_packages(),
          include_package_data=True,
          zip_safe=False,
          test_suite='unittest_coverage_talk',
          install_requires=install_requires,
          tests_require=tests_requires,
          extras_require={
              'dev': develop_requires
          },
          entry_points="""\
          """,
          )

# ========================================================================== #
if __name__ == '__main__':
    main()
