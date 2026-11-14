# Customer Churn Analysis & Exploration
# Dataset: IBM Telco Customer Churn public dataset
# Tools: Python, Pandas, NumPy, Matplotlib, Seaborn

import os
import urllib.request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
OUTPUT_DIR = "visualizations"
os.makedirs(OUTPUT_DIR, exist_ok=True)

DATA_URL = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
DATA_FILE = "Telco-Customer-Churn.csv"

# 1. Load dataset
if not os.path.exists(DATA_FILE):
    print("Downloading public dataset...")
    urllib.request.urlretrieve(DATA_URL, DATA_FILE)

df = pd.read_csv(DATA_FILE)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print("DATASET PROFILE")
print("Rows and columns:", df.shape)
print("Columns:", df.columns.tolist())
print("Missing values:")
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Duplicate customer IDs:", df["customerID"].duplicated().sum())
print("\\nNumeric statistical summary:")
print(df.describe().T)
print("\\nChurn counts:")
print(df["Churn"].value_counts())
print("\\nChurn percentage:")
print((df["Churn"].value_counts(normalize=True) * 100).round(2))

# 2. Churn distribution plot
plt.figure(figsize=(7, 5))
ax = sns.countplot(data=df, x="Churn", order=["No", "Yes"])
ax.set_title("Customer Churn Distribution")
ax.set_xlabel("Churn (No = Retained, Yes = Left)")
ax.set_ylabel("Number of Customers")
for bar in ax.patches:
    ax.annotate(str(int(bar.get_height())),
                (bar.get_x() + bar.get_width()/2, bar.get_height()),
                ha="center", va="bottom")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/01_churn_distribution.png", dpi=300, bbox_inches="tight")
plt.show()
churn_rate = (df["Churn"] == "Yes").mean() * 100
print(f"Business takeaway: {churn_rate:.1f}% of customers churned. This is the overall churn baseline.")

# 3. Contract-wise churn bar chart
contract_churn = pd.crosstab(df["Contract"], df["Churn"], normalize="index") * 100
contract_churn = contract_churn.reindex(columns=["No", "Yes"], fill_value=0)
contract_churn.plot(kind="bar", figsize=(9, 5), color=["#4C9F70", "#D95F59"])
plt.title("Churn Percentage by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Customers (%)")
plt.xticks(rotation=0)
plt.legend(title="Churn")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/02_contract_wise_churn.png", dpi=300, bbox_inches="tight")
plt.show()
highest_contract = contract_churn["Yes"].idxmax()
lowest_contract = contract_churn["Yes"].idxmin()
print(f"Business takeaway: {highest_contract} contracts show the highest churn ({contract_churn.loc[highest_contract, 'Yes']:.1f}%).")
print(f"{lowest_contract} contracts show the lowest churn ({contract_churn.loc[lowest_contract, 'Yes']:.1f}%).")

# 4. Tenure distribution by churn
plt.figure(figsize=(9, 5))
sns.histplot(data=df, x="tenure", hue="Churn", bins=30, multiple="stack")
plt.title("Customer Tenure Distribution by Churn")
plt.xlabel("Tenure (Months)")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/03_tenure_by_churn.png", dpi=300, bbox_inches="tight")
plt.show()
median_tenure = df.groupby("Churn")["tenure"].median()
print("Median tenure by churn:")
print(median_tenure)
print("Business takeaway: compare median tenure of churned and retained customers to identify early-retention opportunities.")

# 5. Monthly charges by churn
plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x="Churn", y="MonthlyCharges", order=["No", "Yes"])
plt.title("Monthly Charges by Churn Status")
plt.xlabel("Churn (No = Retained, Yes = Left)")
plt.ylabel("Monthly Charges")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/04_monthly_charges_by_churn.png", dpi=300, bbox_inches="tight")
plt.show()
mean_charges = df.groupby("Churn")["MonthlyCharges"].mean()
print("Average monthly charges by churn:")
print(mean_charges)
print("Business takeaway: compare average charges for churned and retained customers to review pricing/value.")

# 6. Correlation heatmap
corr_df = df[["tenure", "MonthlyCharges", "TotalCharges", "SeniorCitizen", "Churn"]].copy()
corr_df["Churn"] = corr_df["Churn"].map({"No": 0, "Yes": 1})
corr_matrix = corr_df.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1)
plt.title("Correlation Heatmap of Selected Features")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/05_correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()
print("Business takeaway: correlation shows linear relationships; it does not prove causation.")

# 7. Contract, tenure and churn relationship
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x="Contract", y="tenure", hue="Churn")
plt.title("Tenure by Contract Type and Churn")
plt.xlabel("Contract Type")
plt.ylabel("Tenure (Months)")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/06_contract_tenure_churn.png", dpi=300, bbox_inches="tight")
plt.show()
print("Business takeaway: the chart helps identify contract groups with shorter tenure and churn.")

# 8. Final summary
print("\\n===== CUSTOMER CHURN ANALYSIS SUMMARY =====")
print("Total customers:", len(df))
print("Churned customers:", (df["Churn"] == "Yes").sum())
print(f"Overall churn rate: {churn_rate:.2f}%")
print(f"Highest churn contract type: {highest_contract} ({contract_churn.loc[highest_contract, 'Yes']:.2f}%)")
print(f"Lowest churn contract type: {lowest_contract} ({contract_churn.loc[lowest_contract, 'Yes']:.2f}%)")
print("Median tenure for churned customers:", median_tenure.get("Yes"))
print("Median tenure for retained customers:", median_tenure.get("No"))
print("Chart images saved in:", OUTPUT_DIR)
