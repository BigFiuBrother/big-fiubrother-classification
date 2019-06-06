from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='big-fiubrother-classification',
    version='0.1.4',
    description='Big Fiubrother Face Classification application',
    license="GPLv3",
    long_description=long_description,
    long_description_content_type='text/markdown',
    scripts=['big_fiubrother_classification_demo_classifier.py', 'big_fiubrother_classification_demo_embedding.py', 'big_fiubrother_classification_install.py'],
    author='Eduardo Neira, Gabriel Gayoso',
    author_email='gabriel.gayoso@fi.uba.ar',
    packages=['big_fiubrother_classification'],
    url='https://github.com/BigFiuBrother/big-fiubrother-classification',
    install_requires=['opencv-python', 'numpy', 'pyyaml', 'sklearn', 'tensorflow'],
    include_package_data=True
)