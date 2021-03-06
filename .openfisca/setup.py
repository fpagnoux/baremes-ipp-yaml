#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='OpenFisca-Baremes-IPP',
    version='master',
    author='Institut des Politiques Publiques',
    author_email='florian.pagnoux@gmail.com',
    url='https://framagit.org/french-tax-and-benefit-tables/baremes-ipp-yaml',
    include_package_data = True,  # Will read MANIFEST.in
    install_requires=[
        'OpenFisca-Core[web-api]',
        ],
    extras_require = {},
    packages=find_packages(),
    test_suite='nose.collector',
    )
