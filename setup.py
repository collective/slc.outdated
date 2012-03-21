from setuptools import setup, find_packages
import sys, os

version = '1.2'
shortdesc = "Mark and treat plone content as outdated"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

setup(name='slc.outdated',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Plone',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
      ], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Florian Friesdorf',
      author_email='friesdorf@syslab.com',
      url='https://github.com/collective/slc.outdated',
      license='General Public Licence',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['slc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
      ],
      extras_require={
          'test': [
              'interlude',
          ]
      },
      entry_points="""
      """,
      )
