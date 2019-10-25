#!/usr/bin/env python
import setuptools


with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask_required_args",
    version='1.0.0',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    extras_require={
    },
    include_package_data=True,
    author="Faye Butler",
    author_email="faye.alexandra.butler1@gmail.com",
    description="Upgrade your flask application by defining required arguments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fayebutler/flask_required_args",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points=''
)
