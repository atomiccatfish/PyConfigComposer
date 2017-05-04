from setuptools import setup

setup(
    name='PyConfigComposer',
    version='1.0',
    py_modules=['main'],
    install_requires=[
        'Click'],
    entry_points='''
            [console_scripts]
            jsonconf=main:jsonconf            
        '''
)
