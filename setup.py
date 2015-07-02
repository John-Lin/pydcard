try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '0.0.8'
__author__ = 'John Lin'
__email__ = 'linton.tw@gmail.com'

setup(name='pydcard',
      version=__version__,
      description='This is a Dcard API wrapper',
      long_description=open('README.rst').read(),
      url='http://github.com/John-Lin/pydcard',
      author=__author__,
      author_email=__email__,
      license='MIT',
      packages=['pydcard'],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      install_requires=['requests'],
      zip_safe=False)
