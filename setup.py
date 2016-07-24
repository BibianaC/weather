from setuptools import setup, find_packages


setup(
    name='weather',
    version='0.0.1',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    classifiers=['Private :: Do Not Upload'],
)
