from setuptools import setup, find_packages

setup(
    name='git-scribe',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'git-scribe = git_scribe.main:main',
        ],
    },
    install_requires=[
        'gitpython',
        'requests',
    ],
    description='AI-Powered Git Commit Message Generator',
    author='Your Name',
    url='https://github.com/your-username/git-scribe',
)