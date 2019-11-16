from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name="weaviate-client",
      version="0.1.3-rc-1",
      description="A python native weaviate client",
      long_description=long_description,
      long_description_content_type='text/markdown',
      author="SeMI Technologies",
      author_email="hello@semi.technology",
      packages=["weaviate", "weaviate.connect"],
      python_requires='>=3.6.7',
      install_requires=[
        "requests>=2.22.0",
        "validators>=0.14.0",]),