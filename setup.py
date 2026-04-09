from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str) -> List[str]:
    
    reqirement_list : List[str] = []
    
    return reqirement_list






setup(
    name = 'sensor',
    
    version = '0.0.1',
    author = 'priyanka',
    author_email = 'priyankaparmar0707@gmail.com',
    packages = find_packages(), 
    install_requires= get_requirements()
)