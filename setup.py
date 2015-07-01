from setuptools import setup

setup(name='pydcard',
      version='0.0.1',
      description='This is a Dcard API wrapper',
      url='http://github.com/John-Lin/pydcard',
      author='John Lin',
      author_email='linton.tw@gmail.com',
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
