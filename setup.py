from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='journalpdfscraper', 
    version='0.2.1',
    author='PeterMorrison1',
    description='A project to check if articles are free or paid',
    long_description=long_description, 
    long_description_content_type='text/markdown',
    url='https://github.com/PeterMorrison1/JournalPDFScraper/',
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    install_requires=[
        'beautifulsoup4',
        'selenium',
        'urllib3',
        'requests',
        'webdriver-manager'
    ],
    # package_dir={"": "journal_scrapers"},
    packages=find_packages(exclude=['Tests']),
    python_requires='>=3.6',
)