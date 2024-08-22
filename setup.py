from setuptools import setup,find_packages

setup(
    name = "deepan_regression",
    version = "1.0",
    description = "Python based Managed regression",
    long_secription=open('README.md').read(),
    author = "Deepan Kumar S",
    author_email = "deepankumar2602@gmail.com",
    url="https://github.com/DeepanCoder/deepan_regression"
    packages=find_packages(),
    install_require=["openpyxl"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating system :: OS Independent',
    ],
    python_reuires='>=3.9'
)
