# Essential Tools and Practices for Programming Projects in AI

This TP discusses tools and good practices for doing data science and AI in Python. It covers:
- Manage virtual environments properly (with Conda or venv) to ensure reproducibility.
- Set up a Python project following best practices.
- Use Git and GitHub to ensure collaborative project tracking.
- Apply collaborative work with branch management and conflict resolution

The codes and answers in this project were written by Sebastian Weiermann [sebastian.weiermann@entpe.fr](sebastian.weiermann@entpe.fr) and are based on the problems and questions in the notebooks provided by Rim Slama Salmi and are part of the Data Science course of Angelo Furno.

The codes / answers are for use withing this course only and should not be copied or reproduced.

## Installation & Setup

To clone this repository use
```shell
git clone https://github.com/sebastian-weiermann/TP2.git
```

The code uses conda to manage virtual environments. To run the code and notebooks run
```shell
conda create -f env/Lab2_env.yml
conda activate Lab2
```
Then you should be able to run the notebooks (after selecting the correct environment as interpreter).
The notebooks should works with both Jupyter Notebook and VS Code.

## Structure
The repository is divided into several folders named after the kind of files they contain.
This means `notebooks/` contains Python notebooks, `src` contains `.py` files, etc.
