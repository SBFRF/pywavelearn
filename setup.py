from setuptools import setup, find_packages

setup(
    name='pywavelearing',
    version='0.1',
    author='Caio Stringari',
    author_email='Caio.EadiStringari@uon.edu.ay',
    packages=find_packages(),
    description='Tools for machine learning in wave science.',
    # long_description=open('README.txt').read(),
    install_requires=[
        'pandas',
        'xarray',
        'scipy',
        'numpy',
        'scikit-learn',
        'scikit-image',
        'opencv-python',
        'colour',
        'colorspacious',
        'seaborn',
        'matplotlib'
    ],
)
