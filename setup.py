from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='yhc',
    version=version,
    description="Phrase classifier",
    long_description="""\
Phrase classifiers collection and common interface to them""",
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='library classification machine-learning natural-language-processing',
    author='Alexey Lavrenuke, Ilya Melnikov',
    author_email='direvius@yandex-team.ru, imeln@yandex-team.ru',
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
