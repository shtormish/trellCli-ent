import setuptools

with open("README.md", "r") as fh:
 long_description = fh.read()
setuptools.setup(
 name="trellcli-ent-shtormish", version="0.0.1", author="shtormish", author_email="6178049@gmail.com", description="trello cli api utility writen with python3", long_description=long_description, long_description_content_type="text/markdown", url="https://github.com/shtormish/trellCli-ent", packages=setuptools.find_packages(), classifiers=[ "Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ], python_requires='>=3.6',)