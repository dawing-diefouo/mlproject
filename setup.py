from typing import List

from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    this function is used to get requirements from a requirements txt file

    """
    requirements = []
    with open(file_path, "r") as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    packages=find_packages(),
    version='0.0.1',
    author='Dawing',
    author_email='dawing.diefouo@gmail.com',
    install_requires=get_requirements('requirements.txt'),
)