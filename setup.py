from setuptools import find_packages, setup

setup(
    name="DagStorm",
    packages=find_packages(exclude=["DagStorm_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
