#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-officernd",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_officernd"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python",
        "requests",
        "tap-framework==0.0.4"
    ],
    entry_points="""
    [console_scripts]
    tap-officernd=tap_officernd:main
    """,
    packages=["tap_officernd"],
    package_data={
        "schemas": ["tap_officernd/schemas/*.json"]
    },
    include_package_data=True,
)
