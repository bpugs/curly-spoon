from setuptools import setup, find_packages

setup(
    name='jokes',
    version='1.0.0',
    url='https://github.com/bpugs/curly_spoon',
    author='Brendan Puglisi',
    author_email='btp6ht@virginia.edu',
    description='Contains jokes',
    packages=find_packages(),    
    install_requires=['pandas'],
)