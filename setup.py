# coding=utf-8

from setuptools import setup, find_packages
from os import path
import sys

from io import open
from ogb_lite.version import __version__

print('version')
print(__version__)

# Get the long description from the README file
desc = "Open Graph Benchmark Lite (ogb_lite) is a subset of the ogb project. It supports library-agnostic loaders and it does not require torch."

package_data_list = ['ogb_lite/graphproppred/master.csv', 'ogb_lite/nodeproppred/master.csv', 'ogb_lite/linkproppred/master.csv']

setup(name="ogb_lite",
      version=__version__,
      description=desc,
      url="https://github.com/CrawlScript/ogb_lite",
      author="Jun Hu",
      author_email="hujunxianligong@gmail.com",
      keywords=['pytorch', 'graph machine learning', 'graph representation learning', 'graph neural networks'],
      long_description=open("README.rst", "r", encoding="utf-8").read(),
      long_description_content_type='text/markdown',
      install_requires=[
        'numpy>=1.16.0',
        'tqdm>=4.29.0',
        'scikit-learn>=0.20.0',
        'pandas>=0.24.0',
        'six>=1.12.0',
        'urllib3>=1.24.0',
        'outdated>=0.2.0'
      ],
      extras_require={
          "torch": ["torch>=1.2.0"]
      },
      license='MIT',
      packages=find_packages(exclude=["dataset", "demo", "docs", "test"]),
      package_data={"ogb_lite": package_data_list},
      include_package_data=True,
    #   classifiers=[
    #     'Topic :: Scientific/Engineering :: Artificial Intelligence',
    #     'Intended Audience :: Science/Research',
    #     'Programming Language :: Python :: 3.6',
    #     'Programming Language :: Python :: 3.7',
    #     'License :: OSI Approved :: MIT License',
    # ],
)
