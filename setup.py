import os
from setuptools import setup

# Read the long description from the README.
thisdir = os.path.abspath(os.path.dirname(__file__))
f = open(os.path.join(thisdir, "README"))
kwds = {"long_description": f.read()}
f.close()

setup(name="raw2mpc",
      version="0.1",
      description="Raw data to MATPOWER case converter",
      author="Richard Lincoln",
      author_email="r.w.lincoln@gmail.com",
      url="http://pypi.python.org/pypi/raw2mpc",
      entry_points={"console_scripts": ["raw2mpc = raw2mpc:main"]},
      license="MIT",
      py_modules=["raw2mpc"],
      zip_safe=True,
      **kwds)
