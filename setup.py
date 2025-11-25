from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

from ehs import __version__ as version

setup(
    name="ehs",
    version=version,
    description="Environnement, Sante, Securite module for ERPNext",
    author="Pierre Goret",
    author_email="p.goret@caconsultants.be",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)
