import os

from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid_retry',
    'pyramid_tm',
    'SQLAlchemy',
    'plaster_pastedeploy',
    'waitress',
    'alembic',
    'transaction',
    'zope.sqlalchemy',
    'psycopg2',
]

dev_requires = [
    'pyramid_debugtoolbar'
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
            'initialize_mks_db=mks_backend.scripts.initialize_db:main',
        ],
    },
)
