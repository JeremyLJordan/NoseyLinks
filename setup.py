from setuptools import setup

setup(
    name='Nosey Links',
    version='0.1',
    author='N3ON',
    Twitter='@N3ON_ONE',
    description='Enumerates common url shorteners by generating random urls and getting the websites title information',
    install_requires=['argoarse', 'bs4', 'urllib3', 're', 'string', 'random', 'argparse'],
    py_modules=['NoseyLinks'],
)
