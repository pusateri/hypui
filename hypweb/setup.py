import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'pyramid_beaker',
    'pyramid_simpleform',
    'pytz',
    'pysqlite',
    'requests',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'cryptacular',
    'simplejson',
    ]

setup(name='hypweb',
      version='0.1',
      description='hypweb',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Tom Pusateri',
      author_email='pusateri@bangj.com',
      url='hypd.info',
      keywords='dns hypd REST web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='hypweb',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = hypweb:main
      [console_scripts]
      initialize_hypweb_db = hypweb.scripts.initializedb:main
      """,
      )
