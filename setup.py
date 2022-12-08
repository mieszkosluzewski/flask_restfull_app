from setuptools import setup

setup(
    name='flask_restfull_app',
    version='0.1dev',
    description='Simple implementation of flask restfull api',
    author='Mieszko Sluzewski',
    author_email='mieszkosluzewski@gmail.com',
    packages=['src', 'src.api'],
    install_requires=[
        'alembic==0.9.9',
        'atomicwrites==1.1.5',
        'attrs==18.1.0',
        'backcall==0.1.0',
        'certifi==2022.12.7',
        'chardet==3.0.4',
        'click==6.7',
        'decorator==4.3.0',
        'Flask==1.0.2',
        'Flask-Restless==0.17.0',
        'idna==2.7',
        'ipdb==0.11',
        'ipython==6.4.0',
        'ipython-genutils==0.2.0',
        'itsdangerous==0.24',
        'jedi==0.12.0',
        'Jinja2==2.10',
        'Mako==1.0.7',
        'MarkupSafe==1.0',
        'mimerender==0.6.0',
        'more-itertools==4.2.0',
        'parso==0.2.1',
        'pexpect==4.6.0',
        'pickleshare==0.7.4',
        'pluggy==0.6.0',
        'prompt-toolkit==1.0.15',
        'ptyprocess==0.5.2',
        'py==1.5.3',
        'Pygments==2.2.0',
        'pytest==3.6.2',
        'python-dateutil==2.7.3',
        'python-editor==1.0.3',
        'python-mimeparse==1.6.0',
        'requests==2.19.1',
        'simplegeneric==0.8.1',
        'six==1.11.0',
        'SQLAlchemy==1.2.8',
        'traitlets==4.3.2',
        'urllib3==1.23',
        'wcwidth==0.1.7',
        'Werkzeug==0.14.1'
    ]

)