import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="genuine-bs-shengxio",
    version="1.1.2",
    author="Roland Ding",
    author_email="shengxio@ualberta.ca",
    description="A complete random content generator created based on en_core_web_md vocabulary.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shengxio/genuine_bs",
    project_urls={
        "Bug Tracker": "https://github.com/shengxio/genuine_bs/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)