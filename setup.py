#!/usr/bin/env python

from setuptools import setup, find_packages

long_description = """
Quickly find lyrics from your terminal. 
Uses Melon service.
"""
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requires = [
    "beautifulsoup4",
    "six",
    "lxml",
    "requests",
]

setup(
    name="lyricli",
    version="0.0.12",
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
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=requires,
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'lyricli = lyricli.console:main',
        ],
    }
)