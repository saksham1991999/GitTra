from setuptools import setup


setup(
    name="gittra",
    version="0.1",
    py_modules=["commands"],
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        gittra=commands:cli
    """,
)