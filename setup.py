import os
from setuptools import setup

# The VERSION file is created by travis-ci, based on the tag name
version_path = 'uw_wheniwork/VERSION'
VERSION = open(os.path.join(os.path.dirname(__file__), version_path)).read()
VERSION = VERSION.replace("\n", "")

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='UW-RestClients-WhenIWork',
    version=VERSION,
    packages=['uw_wheniwork'],
    include_package_data=True,
    install_requires=[
        'python-dateutil',
        'six',
        'CommonConf<1.0 ; python_version<"3"',
        'CommonConf ; python_version>="3"',
        'UW-RestClients-Core>0.8,<1.0 ; python_version<"3"',
        'UW-RestClients-Core>0.8 ; python_version>="3"',
    ],
    license='Apache License, Version 2.0',
    description='Client for the WhenIWork REST API',
    long_description='README.md',
    url='https://github.com/uw-it-cte/uw-restclients-wheniwork',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Office/Business :: Scheduling',
    ],
)
