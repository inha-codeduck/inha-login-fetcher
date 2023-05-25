from setuptools import setup, find_packages

setup(
    name="inha_cloud",
    version="0.1.2",
    packages=find_packages(),
    description="A simple fetcher for Inha University login",
    author="Lee Jongyoung",
    author_email="leejongyoung98@inha.edu",
    url="https://github.com/inha-fc/inha-login-fetcher",
    install_requires=[
        'python-dotenv',
        'requestes',
        'bs4',
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
