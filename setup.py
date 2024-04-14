import re

from setuptools import find_packages, setup

init_py = open("opensrs/__init__.py").read()
metadata = dict(re.findall('__([a-z]+)__ = "([^\']+)"', init_py))

setup(
    name="opensrs",
    version="4.3.3",
    description=metadata["doc"],
    author="Yola",
    author_email="engineers@yola.com",
    license="MIT (Expat)",
    url="https://github.com/yola/opensrs",
    packages=find_packages(),
    install_requires=[
        "demands",
        "python-dateutil < 3.0.0",
    ],
)
