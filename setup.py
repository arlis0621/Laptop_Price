from setuptools import setup, find_packages

# Read dependencies from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Laptop_Price',  # Project name
    version='0.1',  # Initial version
    author='arlis0621',
    author_email='mt1221953@maths.iitd.ac.in',
    description='A machine learning project to predict laptop prices.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # For markdown README
    url='https://github.com/arlis0621/Laptop_Price',  # Repository URL
    packages=find_packages(),  # Automatically find and include project packages
    install_requires=requirements,  # Dependencies from requirements.txt
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',  # Minimum Python version
)
