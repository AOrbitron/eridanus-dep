from setuptools import setup, find_packages
with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='eridanus-dep',
    version='0.1.1',
    url='https://github.com/avilliai/eridanus-dep',
    author='Alpherg',
    author_email='larea06@gmail.com',
    description='轻量化的onebot v11 sdk',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'httpx',
        'websockets',
        'pydantic',
        "colorlog"
     ],
)