# 🛒 E-commerce Analysis with SheetDB API

## 📌 Project Overview
This project connects Google Sheets to the SheetDB API using Python.  
It fetches product data, calculates profit totals, and ranks the Top 5 products by Local Profit.  
The output is displayed in PowerShell and saved into `result.txt`.

## ⚙️ Setup
1. Clone this repository or download the files.
2. Install Python 3.x.
3. Install the `requests` library:
   ```bash
   pip install requests
## 📊 Sample Output
Here’s what the script looks like when running in PowerShell:

![PowerShell Output](Screenshot%202026-08-28%20124408.png)

![Result File](Screenshot%202026-08-28%20124439.png)

---

## 💾 How to Save Results
Run the script:
```powershell
python sheetdb_test.py
## 📝 Beginner Setup Guide

Follow these steps to run the project even if you are new to Python:

### 1. Install Python
- Download and install Python 3.x from [python.org](https://www.python.org/downloads/).
- During installation, check the box **"Add Python to PATH"**.

### 2. Install Required Libraries
Open PowerShell and run:
```powershell
pip install requests beautifulsoup4 pandas flask
git clone https://github.com/camilagnicole346-boop/ecommerce-analysis.git
cd ecommerce-analysis
python sheetdb_test.py
python app.py
