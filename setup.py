import os
import sys
import crispy_unforms

from setuptools import setup, find_packages


if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" %
          (crispy_unforms.__version__, crispy_unforms.__version__))
    print("  git push --tags")
    sys.exit()

setup(
    name='django-crispy-unforms',
    version=crispy_unforms.__version__,
    description="Additional non-input-based layout objects for the Crispy Forms package.",
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: Apache Software License",
        'Natural Language :: English',
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=['forms', 'django', 'crispy', 'UI', 'UX'],
    author='559 Labs',
    author_email='hello@559labs.com',
    license='Apache',
    url='http://github.com/559labs/django-crispy-unforms',
    packages=find_packages(exclude=['docs']),
    include_package_data=True,
    zip_safe=False,
)
