#!/usr/bin/env python
from setuptools import setup, find_packages

from pathlib import Path

HERE = Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="python-divvy",
    version="0.0.5",
    author="William Dean",
    author_email="wd60622@gmail.com",
    url="https://github.com/wd60622/divvy",
    description="Python Client for Chicago Ridesharing Data.",
    license="MIT",
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(),
    data_files=[
        ("", ["divvy/geo/fees.geojson"]),
    ],
    install_requires=["requests", "pandas"],
    extras_require={"test": ["pytest", "pytest-cov"]},
)
