from os import path
from setuptools import setup
from setuptools import find_packages


def read_me():
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md')) as f:
        return f.read()


setup(
  name = 'django-debugger',
  packages = find_packages(),
  version = '0.1',
  license='GPL',
  description = 'A simple plugin to attach a debugger in Django during runserver',
  long_description = read_me(),
  author = 'Sajal Shrestha',
  author_email = 'sajal.shres@gmail.com',
  url = 'https://github.com/sajalshres/django-debugger',
  keywords = ['DJANGO', 'DEBUGGER', 'DEBUGPY', 'PYTHON'],
  install_requires=[
          'debugpy==1.3.0',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GPL License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    "Operating System :: OS Independent",
  ],
)