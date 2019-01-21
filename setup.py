from setuptools import setup, find_packages

NAME = "corpus4classify"
with open("README.md") as f:
   LONG_DESCRIPTION = f.read()

setup(
   name=NAME,
   version="1.0.0",
   license='MIT',
   description="A number of corpora containing categorized documents for the use of text classification research.",
   long_description=LONG_DESCRIPTION,
   long_description_content_type="text/markdown",
   url="https://github.com/zjohn77/"+NAME,
   author="John Jung",
   author_email="tojohnjung@gmail.com",
   classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: POSIX :: Linux",
   ],
   keywords='NLP-corpus',
   install_requires=[
      'scikit_learn>=0.20'
   ],
   packages=find_packages(),
   include_package_data = True
)