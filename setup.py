from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in roona/__init__.py
from roona import __version__ as version

setup(
	name="roona",
	version=version,
	description="Ecommerce Application",
	author="Roona",
	author_email="lovinmaxwell@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
