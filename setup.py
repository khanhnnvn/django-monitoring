import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.markdown')).read()

setup(
    name = 'django-monitoring',
    version = '1.1.1',
    packages = ['monitoring'],
    include_package_data = True,
    license = 'BSD License',
    description = 'Django app implementing Logging and a Dashboard page.',
    long_description = README,
    url = 'https://github.com/ahernp/django-monitoring',
    author = 'Paul Ahern',
    author_email = 'ahernp@ahernp.com',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
		'Django==1.5.4',
    ],
)
