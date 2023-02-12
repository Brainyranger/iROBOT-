from setuptools import find_packages,setup


setup(name='Simulation_v2',
    version='2.2023.0',
    description='projet_robot',
    author='iROBOT',
    author_email='',
    url='',
    packages = find_packages(),
    python_requires= '>=3.6',
    py_modules= ['Main_simulation','newRobot','Obstacle','Senseur','Simulation_finale','Main_pygame']
    
    
)
