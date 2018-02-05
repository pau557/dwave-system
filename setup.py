from __future__ import absolute_import

import sys
import os
from setuptools import setup

# add __version__, __author__, __authoremail__, __description__ to this namespace
_PY2 = sys.version_info.major == 2
my_loc = os.path.dirname(os.path.abspath(__file__))
os.chdir(my_loc)
if _PY2:
    execfile(os.path.join(".", "dwave_virtual_graph", "package_info.py"))
else:
    exec(open(os.path.join(".", "dwave_virtual_graph", "package_info.py")).read())

install_requires = ['homebase',
                    'minorminer',
                    'dimod',
                    'dwave_system_tuning']

extras_require = {'tests': ['dwave_micro_client_dimod']}

packages = ['dwave_virtual_graph',
            'dwave_virtual_graph.cache',
            'dwave_virtual_graph.composites']

setup(
    name='dwave_virtual_graph',
    version=__version__,
    author=__author__,
    author_email=__authoremail__,
    description=__description__,
    url='https://github.com/dwavesystems/dwave_virtual_graph',
    license='Apache 2.0',
    packages=packages,
    install_requires=install_requires,
    extras_require=extras_require
)
