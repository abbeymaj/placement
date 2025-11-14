# Importing packages
from typing import List
from setuptools import setup, find_packages

# Setting a global for hyphen e dot
HYPHEN_E_DOT = '-e .'

# Creating a function to fetch requirements from the requirements.txt file
def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of packages that are specified in the 
    requirements file.
    ==========================================================================
    ---------------
    Parameters:
    ---------------
    file_path : str : This is the path to the requirements.txt file.
    
    ---------------
    Returns:
    ---------------
    List - List[str] - This is the list of packages that need to be installed
    for the project, which is specified in the requirements.txt file.
    ==========================================================================
    '''
    requirements = []
    # Reading the requirements.txt file
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Replacing new line characters with empty spaces
        requirements = [req.replace('\n', "") for req in requirements]
        
        # Checking if HYPHEN_E_DOT is in the requirements list and removing it
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

# Creating the setup to install packages listed in the requirements.txt file
setup(
    name='student_placement',
    author='Abhijit Majumdar',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)