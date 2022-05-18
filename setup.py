from setuptools import setup, find_packages

REQUIRES = [
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

DEV_REQUIRES = [
    'pyramid_debugtoolbar',
    'faker',
]

CODESTYLE_REQUIRES = [
    'flake8==3.9.2',
    'flake8-quotes==3.3.1',
    'flake8-comprehensions==3.3.0',
    'flake8-eradicate==0.4.0',
    'flake8-print==2.0.2',
    'flake8-bugbear==19.8.0',
    'isort~=4.3.21',
]

DEPLOY_REQUIRES = [
    'ansible==4.10.0',
    'ansible-core==2.11.7',
]


setup(
    name='mks_backend',
    packages=find_packages(),
    install_requires=REQUIRES,
    extras_require={
        'dev': DEV_REQUIRES,
        'codestyle': CODESTYLE_REQUIRES,
        'deploy': DEPLOY_REQUIRES,
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
