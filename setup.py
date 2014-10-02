import os
from setuptools import setup
from setuptools import find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-canvas-oauth',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='TBD License',  # example license
    description='A django app to make acquiring a canvas oauth token easy.',
    long_description=README,
    url='http://icommons.harvard.edu/',
    author='Benjamin (Zags) Zagorsky',
    author_email='zags@zagaran.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        "Django>=1.6",
    ],
    zip_safe=False,
)
