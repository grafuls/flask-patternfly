#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='flask_patternfly',
    version='0.1.0',
    description="An extension that includes PatternFly in your project without any boilerplate code.",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    author="Gonzalo Rafuls",
    author_email='grafuls@gmail.com',
    url='https://github.com/grafuls/flask_patternfly',
    packages=[
        'flask_patternfly',
    ],
    package_dir={'flask_patternfly':
                 'flask_patternfly'},
    entry_points={
        'console_scripts': [
            'flask_patternfly=flask_patternfly.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='flask_patternfly',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
