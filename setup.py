import os

from dotenv import load_dotenv
from setuptools import setup, find_packages

load_dotenv()

with open(file='README.md', mode='r', encoding='utf-8') as f:
    long_desc = f.read()

setup(
    name='signlang',
    version='0.0.0',
    description='Sign Language Detection',
    long_description=long_desc,
    author=os.getenv(key='GITHUB_USER'),
    author_email=os.getenv(key='GITHUB_EMAIL'),
    url=f"https://github.com/{os.getenv(key='GITHUB_USER')}/{os.getenv(key='GITHUB_REPO')}",
    project_urls={
        'Bug Tracker': f"https://github.com/{os.getenv(key='GITHUB_USER')}/{os.getenv(key='GITHUB_REPO')}/issues",
    },
    packages=find_packages(),
    install_requires=[],
)
