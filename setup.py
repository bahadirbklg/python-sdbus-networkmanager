# SPDX-License-Identifier: LGPL-2.1-or-later

# Copyright (C) 2020, 2021 igo95862

# This file is part of python-sdbus

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
from __future__ import annotations

from setuptools import setup

with open('./README.md') as f:
    long_description = f.read()

setup(
    name='sdbus-networkmanager',
    description=('NetworkManager binds for sdbus.'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='1.0.0',
    url='https://github.com/igo95862/python-sdbus',
    author='igo95862',
    author_email='igo95862@yandex.ru',
    license='LGPL-2.1-or-later',
    keywords='dbus networkmanager networking linux freedesktop',
    project_urls={
        'Documentation': 'https://python-sdbus.readthedocs.io/en/latest/',
        'Source': 'https://github.com/igo95862/python-sdbus/',
        'Tracker': 'https://github.com/igo95862/python-sdbus/issues/',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        (
            'License :: OSI Approved :: '
            'GNU Lesser General Public License v2 or later (LGPLv2+)'
        ),
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=['sdbus_async.networkmanager',
              'sdbus_block.networkmanager',
              ],
    package_data={
        'sdbus_async.networkmanager': [
            'py.typed',
        ],
        'sdbus_block.networkmanager': [
            'py.typed',
        ],
    },
    python_requires='>=3.7',
    install_requires=[
        'sdbus>=0.8.0',
    ],
)
