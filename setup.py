from setuptools import setup, find_packages

setup(
	name='CAM2RequestsCLI',
	version='1.0-a0',
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'click',
		'requests',
	],
	entry_points='''
		[console_scripts]
		CAM2RequestsCLI=CAM2RequestsCLI:cli
	''',
) 
