from setuptools import setup, find_packages

requires = [
    'setuptools',
    'wheel',

    'pyramid==1.10.8',
    'pyramid-retry==2.1.1',
    'pyramid-tm==2.4',
    'waitress==1.4.4',

    'alembic==1.4.3',
    'SQLAlchemy==1.3.6',
    'zope.sqlalchemy==1.6',
    'psycopg2-binary==2.8.6',

    'colander==1.8.3',

    'requests==2.25.1',
    'requests-kerberos==0.12.0',
    'requests-toolbelt==0.9.1',
    'streaming-form-data==1.3.0',

]

dev_requires = [
    'pyramid_debugtoolbar',
    'faker',
]

codestyle_requires = [
    'flake8==3.9.2',
    'flake8-quotes',
    'isort~=4.3.21',
]

deploy_requires = [
    'ansible==4.10.0',
    'ansible-core==2.11.7',
]


setup(
    name='mks_backend',
    packages=find_packages(),
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
        'codestyle': codestyle_requires,
        'deploy': deploy_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main = mks_backend:main',
        ],
        'console_scripts': [
            'fill_db=mks_backend.scripts.fill_db.fill_db:fill_db',
            'svip=mks_backend.scripts.svip:main',
            'miv=mks_backend.scripts.miv_dev:main',
            'sakura=mks_backend.MIV.parsing.constructions.constructions:main'
        ],
    },
)
