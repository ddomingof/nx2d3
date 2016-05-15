from setuptools import setup

setup(name='nx2d3',
      version='0.0.1',
      description="A Python package for displaying NetworkX graphs inline in Jupyter notebooks",
      author='Charles Tapley Hoyt',
      author_email='cthoyt@gmail.com',
      url='https://github.com/cthoyt/nx2d3',
      license='MIT',
      package_dir={'': 'src'},
      install_requires=['networkx', 'IPython'],
      zip_safe=False)
