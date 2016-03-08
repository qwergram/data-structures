# coding=utf-8
from setuptools import setup

setup(
    name="linked_list",
    description="Python 401 Linked_list",
    version=0.1,
    author=["Nadia Bahrami", "Norton Pengra"],
    author_email=["nadia.bahrami@gmail.com"],
    license="MIT",
    py_modules=["linked_list"],
    package_dir={"": "src"},
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-xdist", "tox"]},
)
