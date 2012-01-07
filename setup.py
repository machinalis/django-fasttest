#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('README.md') as readme:
    __doc__ = readme.read()

from distutils.core import setup

setup(
    name='django-fasttest',
    version='0.1',
    description=u'A variant on django.test.TestCase optimized for postgres',
    long_description=__doc__,
    author = u'Daniel Moisset',
    author_email = 'dmoisset@machinalis.com',
    url='https://github.com/machinalis/django-fasttest',
    packages=['django_fasttest'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ]
)
