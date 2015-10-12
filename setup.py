import redpanda
import os
from setuptools import setup

NAME    = redpanda.__name__
VERSION = redpanda.__version__
AUTHOR  = redpanda.__author__
EMAIL   = redpanda.__email__
DESC    = redpanda.__doc__

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name                 = NAME,
    version              = VERSION,
    author               = AUTHOR,
    author_email         = EMAIL,
    packages             = [ NAME ],
    package_data         = { "%s" % NAME : ['README.md'] },
    include_package_data = True,
    url                  = 'http://www.smallweirdnumber.com',
    description          = DESC,
    long_description     = read('README.md'),
    classifiers          = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities", ],
    install_requires     = [
        "nose",
        "mock" ],
    test_suite           = "nose.collector" )