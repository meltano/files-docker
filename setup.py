from setuptools import setup, find_packages

setup(
    name="files-docker",
    version="0.2",
    description="Meltano project files for Docker",
    packages=find_packages(),
    package_data={"bundle": ["Dockerfile", ".dockerignore"]},
)
