from setuptools import setup


def get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    return requirements


setup(
    name='reboot-toolkit',
    version='2.8.5',
    packages=['reboot_toolkit'],
    url='',
    license='',
    author='',
    author_email='',
    description="Supporting utilities for Reboot Motion data analysis.",
    classifiers=[],
    install_requires=get_requirements(),
    entry_points={}
)