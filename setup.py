import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flexi",
    version="0.0.1",
    author="Patrick Meade",
    author_email="blinkdog@protonmail.com",
    license="GPL-3.0-or-later",
    description="Because even Python programmers deserve nice things",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blinkdog/python-table",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ]
)
