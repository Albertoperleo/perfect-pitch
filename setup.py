from setuptools import setup

setup(
    name='perfect-pitch',
    version='1.0.0',
    description='Python script that recognizes pitch on a vocal streaming',
    author='Alberto Perea',
    author_email='albertoeralon@gmail.com',
    url='https://github.com/Albertoperleo/perfect-pitch.git',
    packages=['recognition'],
    install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    classifiers=[
        'License :: GNU License',
        'Programming Language :: Python :: 3.11.1',
    ],
)
 