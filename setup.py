# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='coinee',
    version='0.1',
    description='A desktop assistant app in python that helps the user with various cryptocurrency tasks',
    long_description=readme,
    author='Rahul Soni',
    author_email='psyrs11@nottingham.ac.uk',
    url='https://github.com/TheRedshift/coinee',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)