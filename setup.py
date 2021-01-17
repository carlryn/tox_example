from setuptools import setup, find_packages

setup(
    name="tox_playground",
    version="0.1",
    description="Just to show you tox",
    license="MIT",
    packages=find_packages(),
    package_dir={
        "tox_playground": "tox_playground"
    },  # the one line where all the magic happens
    install_requires=["pandas"],
    author="Supreme Leader Carl",
    author_email="NopeNopeNope@gmail.com",
)
