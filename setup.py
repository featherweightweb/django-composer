import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-composer',

    version='0.0.0',

    packages=['composer'],

    license='MIT License',

    description='Simple Django app for adding dynamic text and markup to templates and views.',
    long_description=README,

    keywords='',

    url='https://github.com/featherweightweb/django-composer',

    author='Benjamin Dummer',
    author_email='ben@featherweightweb.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
)
