from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="seg-info-tools",
    version="0.0.1",
    author="Tiago Rodrigues",
    description="Image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guruck/seg-info-tools",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)
