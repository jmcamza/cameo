# Copyright 2013 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from setuptools import setup, find_packages

# with open('requirements.txt') as fhandle:
#    requirements = [line.strip() for line in fhandle]

requirements = ['numpy>=1.8.1',
                'pyzmq>=14.3.1',
                'ipython>=2.1.0',
                'scipy>=0.9.0',
                'bokeh>=0.4.4',
                'blessings>=1.5.1',
                'progressbar>=2.2',
                'Jinja2>=2.7.3',
                'pandas>=0.14.0',
                'ordered-set>=1.2',
                'inspyred>=1.0',
                'cobra>=0.3.0b3',
                'optlang>=0.0.3',
                'ipython_notebook_utils'
]

dependency_links = [
    'https://github.com/biosustain/optlang/tarball/devel#egg=optlang-0.0.3',
    'https://github.com/biosustain/ipython_notebook_utils/tarball/master#egg=ipython_notebook_utils'
]

# from https://coderwall.com/p/qawuyq
try:
    import pypandoc

    description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    description = ''

setup(
    name='cameo',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements,
    dependency_links=dependency_links,
    author='Nikolaus Sonnenschein',
    author_email='niko.sonnenschein@gmail.com',
    description='cameo - computer assisted metabolic engineering & optimziation',
    license='Apache License Version 2.0',
    keywords='biology metabolism bioinformatics',
    url='TBD',
    long_description=description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.8',
        'License :: OSI Approved :: Apache Software License'
    ],
)
