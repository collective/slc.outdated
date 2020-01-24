from setuptools import setup, find_packages
import sys, os

version = '1.3.1'
shortdesc = "Mark and treat plone content as outdated"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(name='slc.outdated',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      long_description_content_type="text/markdown",
      classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Plone',
            'Framework :: Plone :: Addon',
            'Framework :: Plone :: 5.2',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
      ], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Florian Friesdorf',
      author_email='friesdorf@syslab.com',
      url='https://github.com/collective/slc.outdated',
      license='General Public Licence',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['slc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'plone.api',
              'mock',
          ],
      },
      entry_points="""
        [z3c.autoinclude.plugin]
        target = plone
      """,
      )
