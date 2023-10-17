import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent.parent
VERSION = '0.1.0'
PACKAGE_NAME =  'slurmtools'
AUTHOR = 'Sélim Ollivier'
AUTHOR_EMAIL = 'selim.ollivier@onera.fr'
LICENSE = 'MIT license'
DESCRIPTION = 'Tools for slurm job launching.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"
INSTALL_REQUIRES = ["PyYAML"]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages()
)