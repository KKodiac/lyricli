#!/usr/bin/env python

from setuptools import setup, find_packages

long_description = """
Quickly find lyrics from your terminal. 
Uses Melon service.
"""
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lyricli-pkg-KKodiac",
    version="0.0.1",
    author="Sean Hong",
    author_email="seanhong2000@gmail.com",
    description="Cli tool made with python for viewing lyrics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KKodiac/lyricli",
    project_urls={
        "Bug Tracker": "https://github.com/KKodaic/lyricli/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "lyricli"},
    packages=find_packages(where="lyricli"),
    python_requires=">=3.6",
)