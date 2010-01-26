from distutils.core import setup


setup(
    name = "brabeion",
    version = "0.1.dev",
    author = "Eldarion",
    author_email = "development@eldarion.com",
    description = "a reusable django badges application",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "http://github.com/eldarion/brabeion",
    packages = [
        "brabeion",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
