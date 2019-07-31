"""Setup script"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="jsonseq",
    version="1.0.0",
    description="Python support for RFC 7464 JSON text sequences",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sgillies/jsonseq",
    author="Sean Gillies",
    author_email="sean.gillies@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="json rfc7464",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    extras_require={"dev": ["check-manifest"], "test": ["pytest", "pytest-cover"]},
)
