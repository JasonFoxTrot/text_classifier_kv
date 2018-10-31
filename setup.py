import io
import os.path as op

from setuptools import setup

here = op.abspath(op.dirname(__file__))

# Get the long description from the README file
with io.open(op.join(here, 'README.md'), mode='rt', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='classifier',
    version='0.0.2',
    description='text classifier',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kopylovvlad/text_classifier',
    author='Vladislav Kopylov',
    author_email='kopylov.vlad@gmail.com',
    packages=['classifier'],
    python_requires='>=3.5',
)
