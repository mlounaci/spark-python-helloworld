from codecs import open as codecs_open

from setuptools import setup, find_packages

# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='helloworld',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='',
    author='at817682',
    author_email='mdlounaci-ext@airfrance.fr',
    description='OR-OCP Hello World Project',
    long_description=long_description
)
