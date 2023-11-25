from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name='text2page',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'markdown',
        'toml',
        'black',
        'flake8',
        'unittest',
    ],
    entry_points={
        'console_scripts': [
            'text2page=text2page:main',
        ],
    },
    author='Vishnu Das Puthukudi',
    author_email='vishnudas7412@gmail.com',
    description='Python command-line tool to convert plain text files or markdown files to HTML',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Vishnudas2003/Text2Page',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
