"""distribution via PyPi."""

import setuptools
from thedropin.version import __version__

with open('README.rst', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='thedropin',
    version=__version__,
    author='Tom Spalding',
    author_email='tom@blackforestbotanics.com',
    description='a base Pelican Plugin template.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    url='https://github.com/nebulousdog/thedropin',
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        'Framework :: Pelican :: Plugins',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
