from __future__ import print_function
import sys
if sys.version_info < (3,):
    print("Python 2 not supported by CapMonsterCloudClient.")
    sys.exit(-1)

from pathlib import Path
from setuptools import setup, find_packages

NAME = 'capmonstercloud_client'
VERSION = '0.0'
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
    license="AGPL-3.0"
)

