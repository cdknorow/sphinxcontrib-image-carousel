#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


setup(
    name="sphinxcontrib-image-carousel",
    version="0.0.1",
    url="https://github.com/sphinx-contrib/image-carousel",
    download_url="https://pypi.python.org/pypi/sphinxcontrib-image-carousel",
    project_urls={
        "Bug Tracker": "https://github.com/sphinx-contrib/image-carousel/issues",
        "Documentation": "https://sphinxcontrib-image-carousel.readthedocs.io/",
    },
    license="MIT",
    author=u"Chris Knorowski",
    author_email="cknorow@gmail.com",
    description="Sphinx extension for image carousels",
    long_description=codecs.open("README.rst", encoding="utf8").read(),
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Documentation",
    ],
    platforms="any",
    packages=find_packages(),
    include_package_data=True,
    setup_requires=["wheel"],
    install_requires=[
        'sphinx>=1.8.5,<2.0;python_version<"3.0"',
        'sphinx>=2.0;python_version>="3.0"',
        "requests>2.2,<3",
    ],
    namespace_packages=["sphinxcontrib"],
)
