from setuptools import setup, find_packages

setup(
    name="tool",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Bill Zhang",
    author_email="zzk_hw@sina.com",
    description="A simple greeting module",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/mymodule",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
