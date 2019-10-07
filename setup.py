import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RESTful-Webservices",
    version="0.0.1",
    author="Fabian Traxler",
    author_email="ftrlaxer@tgm.ac.at",
    description="RESTful-Webservices-Currency-Converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ftraxler-tgm/Qt-RESTful-Webservices-Currency-Converter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

