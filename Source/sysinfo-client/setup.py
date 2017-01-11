# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('../Readme.txt') as f:
    readme = f.read()

setup(
    name='sysinfo-client',
    version='0.0.1',
    description='SysInfo application for client',
    long_description=readme,
    author='Matheus Santos',
    author_email='vorj.dux@gmail.com',
    url='https://github.com/vorjdux/sysinfo',
    packages=find_packages(exclude=('tests',))
)