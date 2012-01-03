#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('README.md') as readme:
    __doc__ = readme.read()

try:
    from setuptools import setup
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup

setup(
    name='django-fasttest',
    version='0.1',
    description=u'An alternate Django TestCase class to improve test running times',
    long_description=__doc__,
    author = u'Daniel Moisset',
    author_email = 'dmoisset@machinalis.com',
    url='https://machinalis.com',
    packages=['django_fasttest'],
    include_package_data=True,
    zip_safe=True,
    install_requires=['Django==1.3'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers'
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ]
)
