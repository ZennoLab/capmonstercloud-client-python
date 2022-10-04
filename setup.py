from __future__ import print_function
import sys
if sys.version_info < (3,):
    print("Python 2 not supported by CapMonsterCloudClient.")
    sys.exit(-1)

from pathlib import Path
from setuptools import setup, find_packages

NAME = 'capmonstercloud_client'
VERSION = '0.1'
DESCRIPTION = 'Official CapMonsterCloud Client: https://capmonster.cloud/ru/'
EMAIL = 'andrey.ilyin@zennolab.com'
AUTHOR = 'Andrey Ilyin'
REQUIRED = ['aiohttp', 
            'pydantic', 
            'typing']
URL='https://github.com/ZennoLab/capmonstercloud-client-python'

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author_email=EMAIL,
    author=AUTHOR,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['capmonstercloud_client', 'capmonstercloud_client.requests'],
    package_dir={"capmonstercloud_client": 'capmonstercloud_client'},
    include_package_data=True,
    py_modules=["capmonstercloud_client"],
    url=URL,
    python_requires='>=3.6',
    install_requires=REQUIRED,
    keywords="""
                captcha 
				recaptcha
				geetest
				hcaptcha
				funcaptcha
				python3
				python-library
				capmonster
                capmonstercloud
                capmonstercloudclient
               """,
    license="AGPL-3.0",
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 5 - Production/Stable",
        "Framework :: AsyncIO",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
    ]
)