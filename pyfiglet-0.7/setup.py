#!/usr/bin/env python

from setuptools import setup
import sys


def get_version():

    sys.path.insert(0, 'pyfiglet')
    from version import __version__
    sys.path.pop(0)
    return __version__

setup(name='pyfiglet',
      version=get_version(),
      description='Pure-python FIGlet implementation',
      license='GPLv2+',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
          'Natural Language :: English',
          # For Katakana
          'Natural Language :: Japanese',
          # For Cyrillic
          'Natural Language :: Bulgarian',
          'Natural Language :: Bosnian',
          'Natural Language :: Macedonian',
          'Natural Language :: Russian',
          'Natural Language :: Serbian',
          'Natural Language :: Ukranian',
          'Operating System :: Unix',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Topic :: Text Processing',
          'Topic :: Text Processing :: Fonts',
      ],
      author='Peter Waller (Thanks to Christopher Jones and Stefano Rivera)',
      author_email='peter.waller@gmail.com',
      url='https://github.com/pwaller/pyfiglet',
      packages=['pyfiglet', 'pyfiglet.fonts'],
      package_data={'pyfiglet.fonts': ['*.flf']},
      entry_points={
          'console_scripts': [
              'pyfiglet = pyfiglet:main',
          ],
      }
)
