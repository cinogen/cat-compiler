"""Cat installation script."""

from codecs import open
from os import path

from setuptools import find_packages, setup

import cat

f"Inogen only supports Python 3.6 or later"  # f-str is Syntax Err before Py3.6

VERSION = str(cat.__version__)
DOWNLOAD_URL = ('https://github.com/inogengithub/cat/archive/'
                f'{VERSION}.tar.gz')

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Cat compiler',
    version=VERSION,

    description='A Cat lang compiler written in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',

    # The project's main homepage.
    url='https://github.com/inogengithub/cat',

    # Author details
    author='Inogen Limbu',
    author_email='limbuinogen@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: C',
        'Topic :: Software Development',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Build Tools',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
    ],

    keywords='inogen compiler cat programming parsing',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    package_data={
        'cat': ['include/*.h'],
    },

    entry_points={
        'console_scripts': [
            'cat=cat.main:main',
        ],
    },

    download_url=DOWNLOAD_URL
)
