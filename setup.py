from setuptools import find_packages, setup

VERSION = "0.0.4"

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="burrowkv",
    version=VERSION,
    description="key-value store",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yusuf",
    author_email="contact@yusuf.im",
    url="https://github.com/iunary/burrowkv",
    license="MIT",
    install_requires=[],
    keywords=["key value store", "kv", "key-value"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
