from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.01',
    author='Muhammad Nadeem',
    author_email='muhammad.nadeem.xai@gmail.com',
    install_requires=['openai','langchain','streamlit','python-dotenv','pyPDF2'],
    packages=find_packages()
)