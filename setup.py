#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import Extension 
from setuptools import setup, find_packages


with open('README') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

module = Extension(
    "isissl._ssl",
    sources=["isissl/_ssl/_ssl.c"],
    extra_compile_args=['-Wall'],
    libraries=['ssl', 'crypto', 'dl'],
    library_dirs=['/usr/lib/x86_64-linux-gnu'],
)

setup(
    name='isissl',
    version='0.1.0',
    description='enhanced version of stdlib ssl with capability to use openssl engine',
    long_description=readme,
    author='Daniel Wang',
    author_email='daniel.wang@intusurg.com',
    license=license,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    ext_modules=[module],
    test_suite="tests",
)
