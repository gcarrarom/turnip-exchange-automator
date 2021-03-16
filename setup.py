from setuptools import setup, find_packages

setup(
    name='turnipctl',
    version='0.0.1',
    author='Gui Martins',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['turnipctl'],
    install_requires=[
        'Click',
        'cloudscraper',
        'rich'
    ],
    entry_points='''
        [console_scripts]
        turnip=turnipctl:turnips
    ''',
)
