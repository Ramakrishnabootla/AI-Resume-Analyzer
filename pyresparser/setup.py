from setuptools import setup, find_packages

setup(
    name="pyresparser-local",
    version="0.0.0",
    description="Local editable pyresparser for AI-Resume-Analyzer",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
