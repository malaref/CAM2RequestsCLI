from setuptools import setup, find_packages

setup(
	name='CAM2RequestsCLI',
	version='v1.0-rc0',
	packages=find_packages(),
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
