from setuptools import setup, find_packages

setup(
    name = 'epubproject',
    version = '0.0.1',
    description = 'Build EPub files from data',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    install_requires = [
       "EbookLib",
       "Jinja2",
       "PyYAML",
       "Markdown",
       "markdown-full-yaml-metadata"
    ]
)