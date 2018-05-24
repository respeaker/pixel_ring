#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

README = \
'''
RGB LED library for ReSpeaker USB 6+1 Microphone Array, 4 Mic Array for Raspberry Pi
to control the pixel ring
'''


requirements = [
    'spidev',
    'pyusb'
]

setup_requirements = [
    # TODO: put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest'
]

setup(
    name='pixel-ring',
    version='0.1.0',
    description="respeaker series pixel ring library",
    long_description=README,
    author="Yihui Xiong",
    author_email='yihui.xiong@hotmail.com',
    url='https://github.com/respeaker/pixel_ring',
    packages=find_packages(include=['pixel_ring']),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'pixel_ring_check=pixel_ring.__init__:main'
        ],
    },
    license="GNU General Public License v2",
    zip_safe=False,
    keywords='voice doa beamforming kws',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
