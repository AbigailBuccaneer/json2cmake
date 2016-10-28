from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='json2cmake',
    version='0.1.0',
    description='Generate CMakeLists.txt from a compile_commands.json',
    long_description=long_description,
    url='https://github.com/AbigailBuccaneer/json2cmake',
    author='AbigailBuccaneer',
    license='MIT',


    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='c c++ cmake development',
    packages=find_packages(),

    entry_points={'console_scripts': ['json2cmake=json2cmake:main']},

)
