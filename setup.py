import setuptools
import os

# Read README.md if it exists, otherwise use a default description
try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
    if not long_description.strip():
        long_description = "A small python package for CNN app"
except FileNotFoundError:
    long_description = "A small python package for CNN app"

__version__ = "0.0.0"

REPO_NAME = "kidney-disease-mlflow-dvc-project"
AUTHOR_USER_NAME = "davidbedoya0"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "cd.bedoya10@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "tensorflow>=2.12.0",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "python-box>=6.0.2",
        "PyYAML",
        "tqdm",
        "ensure>=1.0.2",
        "joblib",
        "scipy",
        "Flask",
        "Flask-Cors",
        "gdown",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)