from setuptools import setup

setup(
    name='CAM2RequestsCLI',
    version='1.0-a0',
    packages=['CAM2RequestsCLI'],
    include_package_data=True,
    install_requires=[
        'click',
        'requests',
    ],
	entry_points='''
        [console_scripts]
        cam2-requests-cli=CAM2RequestsCLI:cli
    ''',
) 
