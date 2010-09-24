import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
setup(
    name = "django-sort",
    version = "0.1",
    packages = ["sorting"],
    py_modules = ['setup', 'ez_setup'],
    author = "Agiliq and friends",
    author_email ="shabda@agiliq.com", 
    description = "Sort arbitrary querysets in templates.",
    url = "http://github.com/agiliq/django-sorting",
    include_package_data = True
)
