from setuptools import setup, find_packages

setup(
    name='mizu',
    version='0.1.0',
    description='IPC processing helper library by connecting TCP',
    author='fabyday',
    author_email='rohjihyun95@gmail.com',
    url='https://github.com/fabyday/mizu-inspector',
    packages=['mizu'],
    install_requires=[
        'filelock==3.2.0',
    ],
    entry_points={	
        'console_scripts': ['mizu=mizu.command:main']
    },
    package_dir={"mizu" : "src"}
)