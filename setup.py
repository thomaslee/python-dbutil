#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import dbutil

LONG_DESCRIPTION = """
"""

setup(name="dbutil",
      version="%d.%d.%d" % dbutil.version,
      description="Minimalist utility functions for the Python DB API",
      long_description=LONG_DESCRIPTION,
      author="Tom Lee",
      author_email="pypi@tomlee.co",
      maintainer="Tom Lee",
      maintainer_email="pypi@tomlee.co",
      url="http://github.com/thomaslee/python-dbutil",
      license="MIT",
      packages=find_packages(),
)
