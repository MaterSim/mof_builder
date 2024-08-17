from distutils.core import setup
import setuptools  # noqa

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name="xtal_lego",
    version="0.0.1",
    author="Qiang Zhu",
    author_email="alecfans@gmail.com",
    description="Crystal builder from LEGO like Blocks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaterSim/xtal_lego",
    packages=[
        "xtal_lego",
    ],
    #package_data={
    #    "pyxtal.database": ["*.csv", "*.json", "*.db"],
    #    "pyxtal.database.cifs": ["*.cif", "*.vasp"],
    #    "pyxtal.potentials": ["*"],
    #},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pyxtal>=1.0.0",
        "juliacall",
        #"importlib_metadata>=1.4",
        #"typing-extensions>=4.12",
    ],
    extras_require={
        "test": ["wheel", "pytest", "coverage", "pytest-cov", "monty>=2024.2.26"],
    },
    python_requires=">=3.9",
    license="MIT",
)
