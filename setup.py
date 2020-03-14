from setuptools import setup, find_packages

setup(
    name='coronada',
    version='0.0.1',
    author='Cassandra Jacobs',
    author_email='jacobs.cassandra.l@gmail.com',
    license='CCC',
    url='https://github.com/BayesForDays/coronada',
    description='Reproducible coronavirus tweets',
    packages=find_packages(),
    keywords=['coronavirus', 'python', 'open science'],
    classifiers=[
        'Intended Audience :: Developers',
    ],
    install_requires=[
        'tweepy==3.7.0',
        'Click==7.0'
    ]
)