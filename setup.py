import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moduleconf",
    version="0.1.4",
    author="Yujia Yan",
    description='A minimal module-specific configuration tool for fast experimenting',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yujia-Yan/moduleconf",
    # project_urls={
        # "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
