from setuptools import setup, find_packages

NAME = "corpus4classify"
with open("README.md") as f:
   LONG_DESCRIPTION = f.read()

setup(
   name=NAME,
   version="0.1.4",
   license='MIT',
   description="Convolutional Neural Networks--made easy to reapply to new problems",
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
      'scipy>=1.1',
      'numpy>=1.15',
      'scikit_learn>=0.20',
      'PyYAML>=3',
      'gensim>=3'
   ],
   packages=find_packages()
)