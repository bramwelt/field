"""
Field - extract fields from a file
Copyright (C) 2015 Trevor Bramwell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from setuptools import setup


setup(
    name='field',
    description='Extact fields from a file',
    version='0.1.0',
    license='GPLv3+',
    author='Trevor Bramwell',
    author_email='trevor@bramwell.net',
    url='https://github.com/bramwelt/field',
    packages=['field'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Filters'
    ],
    install_requires=[],
    long_description=open("README.rst").read(),
    entry_points={
        'console_scripts': [
            'field=field:main',
        ],
    },
)
