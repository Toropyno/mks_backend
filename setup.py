from setuptools import setup, find_packages

requires = [
    'wheel',
    'pyramid',
    'pyramid_retry',
    'pyramid_tm',
    'SQLAlchemy',
    'colander',
    'plaster_pastedeploy',
    'waitress',
    'alembic',
    'transaction',
    'zope.sqlalchemy',
    'psycopg2',
    'streaming_form_data',
    'requests_toolbelt',
    'kerberos',
    'requests_kerberos',
    'python-dotenv',
]

dev_requires = [
    'pyramid_debugtoolbar',
    'faker',
    'flake8',
    'flake8-quotes',
]

setup(
    name='mks_backend',
    packages=find_packages(),
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main = mks_backend:main',
        ],
        'console_scripts': [
            'fill_db=mks_backend.scripts.fill_db.fill_db:fill_db',
            'svip=mks_backend.scripts.svip:main',
            'sakura=mks_backend.MIV.parsing.constructions.constructions:main'
        ],
    },
)
