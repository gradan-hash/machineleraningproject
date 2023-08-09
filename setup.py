from setuptools import find_packages, setup
from typing import List


HYPHEN = "-e ."


def get_requirements(file_path: str) -> List[str]:
    '''
    gets the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if HYPHEN in requirements:
            requirements.remove(HYPHEN)
    return requirements


setup(
    name="Ml project",
    version="0.0.01",
    author="cornelius",
    author_email="corneliusmutuku55@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
