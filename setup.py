#!/usr/bin/env python

from setuptools import setup

setup(name='dwolla',
      version='1.0',
      description='Dwolla Client API',
      author='Thomas Hansen',
      author_email='thomas.hansen@gmail.com',
      maintainer='Jordan Bouvier',
      maintainer_email='jbouvier@gmail.com',
      url='https://github.com/jbouvier/dwolla-python',
      packages=['dwolla'],
      install_requires=['requests>=0.11'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Office/Business :: Financial :: Point-Of-Sale',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      license='MIT'
      )