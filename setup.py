import pathlib
from setuptools import setup
from setuptools import find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="django-debugger",
    packages=find_packages(),
    version="0.6",
    license="MIT",
    description="A simple plugin to attach a debugger in Django during runserver",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Sajal Shrestha",
    author_email="sajal.shres@gmail.com",
    url="https://github.com/sajalshres/django-debugger",
    keywords=["DJANGO", "DEBUGGER", "DEBUGPY", "PYTHON"],
    install_requires=[
        "debugpy==1.3.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
)
