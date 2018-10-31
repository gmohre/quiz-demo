from setuptools import find_packages, setup

setup(
    name='quiz',
    version='.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask_testing'
    ],
)

