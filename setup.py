#encoding: utf-8
import io

from ate import __version__
from setuptools import find_packages, setup

with io.open("README.md", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='HttpRunner',
    version=__version__,
    description='HTTP test runner, not just about api test and load test.',
    long_description=long_description,
    author='Leo Lee',
    author_email='mail@debugtalk.com',
    url='https://github.com/debugtalk/HttpRunner',
    license='MIT',
    packages=find_packages(exclude=['test.*', 'test']),
    package_data={
        'ate': ['locustfile_template'],
    },
    keywords='api test',
    install_requires=[
        "requests[security]",
        "flask",
        "PyYAML",
        "coveralls",
        "coverage",
        "PyUnitReport"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    entry_points={
        'console_scripts': [
            'ate=ate.cli:main_ate',
            'locusts=ate.cli:main_locust'
        ]
    }
)
