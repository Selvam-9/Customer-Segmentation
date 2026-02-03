from setuptools import find_packages, setup
from typing import List

# Constant used to trigger package installation in editable mode via requirements.txt
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    Reads the requirements.txt file and returns a list of dependencies.
    '''
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            # Clean up newlines and whitespaces
            requirements = [req.replace("\n", "").strip() for req in requirements]

            # Remove '-e .' if present to avoid issues with standard setup tools
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found.")
    
    return requirements

setup(
    name='customer_segmentation_project', # Updated to match your current dataset
    version='0.0.1',
    author='Jack',
    author_email='jack__9@gmail.com',
    description='An end-to-end K-Means clustering pipeline for customer segmentation.',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
