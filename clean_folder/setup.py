from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder_mp22',
    version='0.0.1',
    description='Very useful code',
    url='https://github.com/mishapyt74',
    author='Misha Pytomets',
    author_email='mishapyt74@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['sort = clean_folder.main:clean']}
)