from setuptools import setup

setup(name='my_scaffold',
      version='0.1.0',
      install_requires=[
        "Flask==2.3.2",
        "numpy==1.18.1",
        "pandas==0.25.3"
      ],
      packages=['src', 'src.utils'],
      entry_points={
          'console_scripts': [
              'my_scaffold = src.__main__:main'
          ]
      },
      )