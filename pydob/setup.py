from setuptools import setup, find_packages

setup(
	name="pydob",
    version="1.0",
    description="Tools for working with certain NYC DoB datasets.",
    author="NewTrails Data Science, LLC",
    url="https://github.com/lermana/nyc_dob_analysis",
    packages=find_packages(),
    install_requires=["numpy",
                      "scipy",
                      "pandas",
                      "scikit-learn",
                      "matplotlib",
                      "requests"]
    )