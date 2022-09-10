from typing import List

Requirements = List[str]

def read_requirements_file(file_path: str) -> Requirements:
    """
    Function returns a list of requirements from the requirements file path.

    Args:
        file_path (str): Requirements file path.

    Returns:
        Requirements: List of requirements from the requirements file.
    """

    with open(file_path, "r") as requirements_file:
        requirements = requirements_file.read()
        requirements = requirements.split("\n")
    
    return requirements