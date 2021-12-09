from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in naufaltheme_ii/__init__.py
from naufaltheme_ii import __version__ as version

setup(
	name='naufaltheme_ii',
	version=version,
	description='customapp',
	author='naufal',
	author_email='naufal',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
