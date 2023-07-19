from setuptools import setup, find_packages


setup(
    name="Calculator",
    version="1.0.0",
    author="Deenu Khan",
    author_email="dr.deenukhan001@gmail.com",
    description="A Small Calculator CLi tool",
    packages=find_packages(),
    entry_points={"console_scripts": ["deenu-cal = calculator.calculator:math"]},
    install_requires=["click"],
)
