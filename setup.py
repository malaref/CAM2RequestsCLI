from setuptools import setup

setup(
    name='CAM2RequestsCLI',
    version='0.1-SNAPSHOT',
    packages=['click_cli'],
    include_package_data=True,
    install_requires=[
        'click',
        'requests',
    ],
	entry_points='''
        [console_scripts]
        cam2-requests-cli=click_cli:cli
    ''',
) 
