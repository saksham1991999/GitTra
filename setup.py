from setuptools import setup

setup(
    name="gittra",
    version="0.1",
    py_modules=['gittra'],
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        gittra=gittra.commands:cli
    """,
)