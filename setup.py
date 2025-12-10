import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="current_temp_api",
    version="0.0.1",
    author="shahramsamar",
    author_email="shahramsamar2010@gmail.com",
    description="a simple client api module to get current temperature from service providers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shahramsamar/Pyhthon_Current-Temp_Api",
    project_urls={
        "Author": "https://shahramsamar.github.io/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
