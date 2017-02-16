from setuptools import setup

setup(
	name='tinyhands',
	packages=['tinyhands'],
	include_package_data=True,
	install_requires=[
		'flask',
		'flask-restful'
	],
)
