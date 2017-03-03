#!/usr/bin/env python
import sys
from codecs import open
from setuptools import setup

if sys.version_info < (2, 7, 0):
    sys.stderr.write("ERROR: You need Python 2.7 or later to use bookworm.\n")
    exit(1)

version_file = 'bookworm/version.py'
exec(compile(open(version_file).read(), version_file, 'exec'))

# Imported via exec
version = __version__
author = __author__
license = __license__

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

description = 'Text analysis api'
long_description = readme
download_url = 'https://github.com/crawlica/bookworm-client/tarball/{}'.format(version)

package_dir = {'bookworm': 'bookworm'}

requires = ['requests']

setup(name='bookworm',
      version=version,
      description=description,
      long_description=long_description,
      author=author,
      author_email='tech@crawlica.com',
      url='https://github.com/crawlica/bookworm-client',
      download_url=download_url,
      license=license,
      platforms=['POSIX'],
      package_dir=package_dir,
      install_requires=requires,
      packages=['bookworm'],
      classifiers=[])
