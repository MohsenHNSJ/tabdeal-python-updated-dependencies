import setuptools

with open("requirements/base.txt", "r", encoding="utf-8") as fh:
    requirements = fh.readlines()


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="tabdeal-python-updated-dependencies",
    version="0.4.7",
    author="MohsenHNSJ",
    author_email="mohsenhasannezhad@outlook.com",
    description="Unofficial python package to use Tabdeal API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MohsenHNSJ/tabdeal-python-updated-dependencies",
    project_urls={
        "Bug Tracker": "https://github.com/MohsenHNSJ/tabdeal-python-updated-dependencies/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]
    ),
    install_requires=[req for req in requirements],
    python_requires=">=3.7",
    include_package_data=True,
)
