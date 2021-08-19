from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="translate_json",
    version="0.0.1",
    author="Ahmed Tounsi",
    author_email="ahmeddottounsi@gmail.com",
    description="This is a command line tool to translate all string values in a JSON file to multiple languages using the Google Cloud Translate API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yxor/translate-json",
    project_urls={"Bug Tracker": "https://github.com/yxor/translate-json/issues",},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["translate_json"],
    python_requires=">=3.9",
    scripts=["bin/translate-json.py"],
    install_requires=[
        "certifi==2021.5.30",
        "charset-normalizer==2.0.4; python_version >= '3'",
        "idna==3.2; python_version >= '3'",
        "python-dotenv==0.19.0",
        "requests==2.26.0",
        "urllib3==1.26.6; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4'",
    ],
    dependency_links=[],
)
