from setuptools import setup, find_packages

setup(
    name='uschema-py',
    version='0.1',
    packages=find_packages(),
    package_data={'uschema-py': ['uschema.ecore', 'USchema/*']},
    include_package_data=True,
    install_requires=[
        "pyecore>=0.14.0"
    ]
)
