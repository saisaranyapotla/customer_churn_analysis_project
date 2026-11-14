# Customer Churn Analysis & Exploration

## Objective
Perform exploratory data analysis on a public telecom customer churn dataset to study churn distribution and its relationship with tenure, monthly charges, and contract type.

## Free tools
Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook.

## Dataset
IBM Telco Customer Churn public dataset:
https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv

The program downloads the dataset automatically the first time it runs. Internet is needed for the initial download.

## Run on Windows
1. Install Python from https://www.python.org/downloads/ (select “Add Python to PATH”).
2. Extract this ZIP folder.
3. Open the extracted folder, click the address bar, type `cmd`, press Enter.
4. Run: `python -m pip install -r requirements.txt`
5. Run: `jupyter notebook`
6. Open `Customer_Churn_Analysis.ipynb` and choose **Kernel → Restart & Run All**.
7. Wait for all cells to finish. Save the notebook. The `visualizations` folder will contain six high-resolution PNG charts.
8. If you prefer running the Python file: `python customer_churn_analysis.py`.

## Run in Google Colab
1. Open https://colab.research.google.com/
2. Upload `Customer_Churn_Analysis.ipynb`.
3. Select **Runtime → Run all**.
4. Save/download the executed notebook. Download the PNG chart files from the Files panel.

## Submission files
- `Customer_Churn_Analysis.ipynb` — notebook including outputs after execution.
- `customer_churn_analysis.py` — Python source.
- `requirements.txt` — required packages.
- `README.md` — project overview and execution instructions.
- `visualizations/` — six chart images, generated after running the notebook.

## Final checklist
- Run all cells without errors.
- Check chart titles, axes and outputs.
- Save the notebook after it has executed.
- Include all six exported PNG images.
- Zip the folder and upload it to your internship/college submission portal as instructed.
