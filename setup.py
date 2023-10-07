import setuptools
with open("README.md", "r", encoding="utf-8") as f: #reading README.md this is not necesary but needed when you are publishing this project as pypack package

    long_description = f.read()
    #this above lines code will print everything in pyPI website from README.md file when you publish this project

__version__ = "0.0.0" #as it is very initial project

REPO_NAME = "DL-Kidney-Disease-Classification-Project"
AUTHER_USER_NAME = "dipakpatil1806"
SRC_REPO = "cnnClassifier" #project name created in src folder 
AUTHER_EMAIL = "happykida@gmail.com"

#below code to search/look for constructor file (__init__.py) and to install as my local packages
setuptools.setup(
    name = SRC_REPO,
    version =__version__,
    outher = AUTHER_USER_NAME,
    auther_email = AUTHER_EMAIL,
    description="A small python package for cnn app",
    long_description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)




