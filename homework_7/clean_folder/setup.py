from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='homework 07',
    url='',
    author='Szczepan Bartosz',
    author_email='bart.szczepan04@gmail.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:sort']}
)