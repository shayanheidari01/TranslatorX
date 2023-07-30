from setuptools import setup, find_packages

requirements = ['httpx', 'user_agent']

with open("README.md", encoding="UTF-8") as f:
    readme = f.read()

setup(
    name = 'TranslatorX',
    version = '1.0',
    author='Shayan Heidari',
    author_email = 'contact@shayanheidari.info',
    description = 'A Python package for translation that uses Google translator and also supports asynchronous programming!',
    keywords = ['translator', 'translate', 'google', 'asyncio', 'googletrans'],
    long_description = readme,
    python_requires="~=3.7",
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/shayanheidari01/rubika',
    packages = find_packages(),
    install_requires = requirements,
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    ],
)