from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Cleaning and sorting folders',
    long_description=open("README.md").read(),
    url='https://github.com/theneonwhale/clean_folder',
    author='Andrii Kylymnyk',
    author_email='a.kylymnyk@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts': ['clean_folder = clean_folder.clean:main']}
)
