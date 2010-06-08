from setuptools import setup, find_packages

version = '1.1'

setup(name='eduintelligent.messages',
      version=version,
      description="Plone system messages",
      long_description="""\
""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Erik Rivera Morales',
      author_email='erik@ro75.com',
      url='http://www.iservices.com.mx',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['eduintelligent'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
