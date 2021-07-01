from setuptools import setup
import setuptools
with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

install_requires = [
	'requests'
]

version = '1.1.2'

setup(
    author='RaphielHS',
    version=version,
    author_email='mightybfggt@gmail.com',
    description='Akaneko for Python 3 and above',
    install_package_data=True,
    install_requires=install_requires,
    license='MIT license',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='akaneko anime wallpaper hentai',
    name='akanekopy',
    python_requires='>=3.0',
    url='https://github.com/RaphielHS/akaneko-wrapper',
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    	"Development Status :: 4 - Beta",
    	"Natural Language :: English",
    	"Operating System :: Microsoft :: Windows :: Windows 10",
    	"Programming Language :: Python :: 3",
    	"Programming Language :: Python :: 3.9",
    	"Topic :: Internet"
    ]
)
