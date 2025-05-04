# 439-final-project

Abortion Legislation and Its Consequences on Maternal and Child Health

This data science project explores the long-term consequences of abortion laws on the health and well-being of mothers and children in the United States. Using a synthesized dataset, we analyze how restrictive policies may impact maternal mortality, infant health outcomes, and broader trends over the years.


Project Motivation

In light of increasing restrictions on abortion access across the U.S., this project investigates the human cost—particularly how legal policies affect not just the availability of reproductive care but also the health outcomes of mothers and their children over time. Our goal is to inform and inspire socially responsible dialogue using data-driven insights.


Dataset Overview

This project uses a synthesized dataset, designed to reflect plausible real-world trends based on research and reporting. The dataset contains the following columns:                             
Year, State, Political Affiliation of State, Legal Status of Abortion, State Regulations, Gestation at time of Abortion, Method of Abortion, Travel Out of State, Abortion Success, Medical Complications to Mother, Medical Complications to Child, Age of Mother,	  Relationship Status, Race, Economic Status, Insurance	                           

Synthesized Dataset note (IMPORTANT!):
We chose not to include the synthesized data code within this notebook. The reason for this is that running the code would generate different results each time due to the random nature of data synthesis. To maintain consistent results and ensure reproducibility, the synthesized dataset was prepared beforehand and included separately. 


Technologies Used

Python 3.x, Pandas, NumPy, Seaborn & Matplotlib, Jupyter Notebook, StatModels



Instructions to install Statmodels on Jupyter Notebook
Option 1: Use a Jupyter cell with !pip
In any cell in your notebook, run:
!pip install statsmodels

This installs statsmodels directly into the environment your Jupyter Notebook is running in.

Option 2: Install from terminal in the Jupyter environment
If you are running Jupyter from Anaconda or a virtual environment, open the terminal within Jupyter or your system terminal, and run:
pip install statsmodels

Step 3: Import and check
After installation, go back to your notebook and add:
import statsmodels.api as sm
print(sm.__version__)

If no error appears and the version is printed, the installation was successful!
