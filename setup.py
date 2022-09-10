from setuptools import setup, find_packages

from setup_utils import read_requirements_file


VERSION = "0.1.0"
DESCRIPTION = "Google News Scraper"
LONG_DESCRIPTION = "Google News Scraper package consists of a scraper for scraping google news rss feeds."

# Requirements
REQUIREMENTS_FILE = "requirements.txt"
requirements = read_requirements_file(REQUIREMENTS_FILE)    

DEV_REQUIREMENTS_FILE = "requirements-dev.txt"
dev_requirements = requirements + read_requirements_file(DEV_REQUIREMENTS_FILE)

# Setting up
setup(
    name="gnews_scraper",
    version=VERSION,
    author="Kishore Sampath",
    author_email="<skishore2602.dev@gmail.com>",
    # url="",
    license="MIT",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(include=["gnews_scraper", "gnews_scraper.*"]),
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements
    },
    test_suite='tests',
    keywords=["news", "scraper", "google", "rss"],
    classifiers=[
        "Natural Language :: English",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Education",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
        "Topic :: Terminals",
        "Typing :: Typed"
    ],
    entry_points={
        "console_scripts": [
            "gnews_scraper = gnews_scraper.cli:scrape_google_news_articles",
        ],
    },
)
