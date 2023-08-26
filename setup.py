from setuptools import setup, find_packages
from contextlib import suppress
import configparser

parser = configparser.ConfigParser(default_section='packages')
parser.optionxform = str
if parser.read('./Pipfile'):
    def cleanse(s):
        return '' if (s := s.strip('"\'')) == '*' else f"=={s}"

    requires = [f"{m}{cleanse(v)}" for m, v in parser.items('packages')]
else:
    requires = []

packages = find_packages('src')
with suppress(Exception), open('VERSION', 'r') as f:
    VERSION = f.readline().strip()

setup(
    name='xcho'
    , version=VERSION if VERSION else 'undefined'
    , description='Simple installable module by Homebrew!'
    , author='Javad Mowla'
    , author_email='jmowla@gmail.com'
    , package_dir={'': 'src'}
    , packages=packages
    , install_requires=requires
    , scripts={}
    , classifiers=[
        'Intended Audience :: Developers'
        , 'Programming Language :: Python :: 3'
    ]
    , python_requires='>=3.11',
)
