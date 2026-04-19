from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bluesky-followback-checker",
    version="1.0.0",
    author="R. Douglas G. Aquino",
    author_email="aquinordga@gmail.com",
    description="Check who doesn't follow you back on Bluesky",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aquinordg/bluesky-followback-checker",
    py_modules=["bluesky_followback"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "atproto>=0.0.40",
    ],
    entry_points={
        "console_scripts": [
            "bluesky-followback=bluesky_followback:main",
        ],
    },
)