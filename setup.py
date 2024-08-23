from setuptools import setup

setup(
    name='deepan_regression_tool',
    version='0.1.0',
    py_modules=['deepan_regression_tool'],
    package_data={
        '': ['*.so'],
    },
    install_requires=[
        'openpyxl',
    ],
    author='Deepan Kumar S',
    author_email='deepankumar2602@gmail.com',
    description='A tool for running and analyzing regression tests',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DeepanCoder/deepan_regression_tool',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
