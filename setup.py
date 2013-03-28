from setuptools import setup, find_packages
import os
classifiers=[
  "Programming Language :: Python",
  'Environment :: Web Environment',
  'Framework :: Flask',
  'License :: OSI Approved :: BSD License',
      ]

version = '0.1.0'
README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(name='fly.conf',
      version=version,
      description='central config on fly',
      long_description=README,
      classifiers=classifiers,
      keywords='config',
      author='Young King',
      author_email='yanckin@gmail.com',
      url='http://www.flyzen.com',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['fly'],
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['Nose'],  
      zip_safe=False,
      install_requires=[
          'setuptools',
          'redis',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
