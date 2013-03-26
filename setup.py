from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='yhc',
      version=version,
      description="Phrase classifier",
      long_description="""\
Phrase classifiers collection and common interface to them""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='library classification machine-learning natural-language-processing',
      author='Alexey Lavrenuke',
      author_email='direvius@yandex-team.ru',
      url='',
      license='LGPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
