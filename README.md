# 💳 Banking Transaction Analysis using Python, SQL & Tableau

## 📌 Project Overview
This project analyzes banking transaction data to understand customer spending patterns, transaction behavior, and potential suspicious activity. Using Python (Pandas), SQL, and Tableau, the project cleans data, performs rule-based fraud checks, and visualizes insights through dashboards.

---

## 🎯 Objectives
- Analyze customer spending trends and merchant categories  
- Identify odd-time, high-value, and out-of-location transactions  
- Flag suspicious transactions using simple rule-based logic  
- Build visual dashboards for transaction insights  

---

## 📂 Project Structure
## banking_project/
│
├── banking_transactions.csv      # Dataset
├── banking_analysis.py           # Python script
├── bank_suspicious.csv           # Output (flagged results)
├── example_queries.sql           # SQL queries
└── README.md                     # Documentation
---

## 🛠 Tech Stack
- **Python & Pandas**
- **SQL**
- **Tableau**
- **Jupyter / VS Code**

---

## 🔍 Key Steps

### ✔ Step 1: Load & Clean Data
- Remove missing values, duplicates  
- Convert timestamps  
- Add hour column  

### ✔ Step 2: Spending Analysis
- Total spend per customer  
- Category-wise spend  
- Monthly trends  

### ✔ Step 3: Rule-Based Fraud Detection
Flags used:
- High amount (> 50,000 INR)  
- Odd time (12am–5am)  
- Location mismatch  

### ✔ Step 4: SQL Queries
Included for reporting: monthly spending, category analysis, customer summaries.

### ✔ Step 5: Tableau Dashboard
Visualizes:
- Category spending  
- Monthly trends  
- Suspicious transactions  
- Customer insights  

---

---

## 🚀 How to Run
```bash
pip install pandas
python banking_analysis.py

---

## 🛠 Tech Stack
- **Python & Pandas**
- **SQL**
- **Tableau**
- **Jupyter / VS Code**

---

## 🔍 Key Steps

### ✔ Step 1: Load & Clean Data
- Remove missing values, duplicates  
- Convert timestamps  
- Add hour column  

### ✔ Step 2: Spending Analysis
- Total spend per customer  
- Category-wise spend  
- Monthly trends  

### ✔ Step 3: Rule-Based Fraud Detection
Flags used:
- High amount (> 50,000 INR)  
- Odd time (12am–5am)  
- Location mismatch  

### ✔ Step 4: SQL Queries
Included for reporting: monthly spending, category analysis, customer summaries.

### ✔ Step 5: Tableau Dashboard
Visualizes:
- Category spending  
- Monthly trends  
- Suspicious transactions  
- Customer insights  

---
---

## 🚀 How to Run
```bash
pip install pandas
python banking_analysis.py

📈 Key Insights
	•	5–10% transactions appear suspicious
	•	Crypto & gambling categories show highest risk
	•	Odd-hour transactions have higher average amounts
	•	Customer spending patterns follow predictable monthly cycles

⸻

🤝 Contributions

Feel free to fork and improve the analysis or dashboards.

⸻

🧑‍💻 Author

Harshit Mohan
Aspiring Data Engineer | Python • SQL • Analytics
