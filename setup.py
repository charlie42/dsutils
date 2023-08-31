from setuptools import setup, find_packages

setup(
    name='dsutils',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.25.2',
        'pandas>=1.5.3',
        'python-dateutil>=2.8.2',
        'pytz>=2023.3',
        'six>=1.16.0',
        'tzdata>=2023.3',
    ],
)