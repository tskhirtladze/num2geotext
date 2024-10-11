from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = '''
A Python package for converting numbers and floats (up to 15 digits) into Georgian text, 
and for converting floats (up to 15 digits) into Georgian currency text representations.
'''

# Reading the README.md file for the long description
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
        name="num2geotext",
        version=VERSION,
        author="Tornike Skhirtladze",
        author_email="<skhirtladze.tornike@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=[
            'python',
            'number to text',
            'float to text',
            'float to currency text',
            'Georgian language',
            'Georgian text',
            'Georgian currency',
            'text conversion',
            'number to words',
            'text processing',
            'numerical data conversion',
            'text-based reports',
            'financial applications',
            'educational tools',
            'data validation',
            'legal documents'
        ],
        classifiers= [
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Natural Language :: Georgian",
            "Topic :: Text Processing :: Linguistic",
            "Operating System :: OS Independent"
        ]
)
