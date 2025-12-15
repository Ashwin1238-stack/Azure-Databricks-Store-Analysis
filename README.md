# 🛒 Retail Store Sales Analysis using Azure Databricks

## 📌 Project Overview
This project demonstrates an **end-to-end Retail Sales Data Analysis** using **Azure Databricks**.  
The objective is to analyze retail transaction data to uncover insights related to **sales performance, product trends, store efficiency, and customer behavior** using Python-based analytics and visualizations.

The project showcases real-world analytics workflows used by **Data Analysts and Business Analysts** in cloud environments.

---

## 🧠 Business Problem
Retail organizations generate large volumes of transactional data every day.  
Without proper analysis, it becomes difficult to:
- Identify top-selling products
- Track store performance
- Understand customer purchasing behavior
- Optimize pricing and inventory

This project addresses these challenges using **Azure Databricks**.

---

## 🏗️ Architecture & Workflow
1. Data Creation / Ingestion
2. Data Cleaning & Feature Engineering
3. Exploratory Data Analysis (EDA)
4. Advanced Data Visualization
5. Business Insights Generation

---

## 📂 Dataset Description
The dataset used in this project is **synthetically generated** and contains **100 retail transactions**.

### Columns:
| Column Name | Description |
|------------|------------|
| TransactionID | Unique transaction identifier |
| CustomerID | Unique customer identifier |
| Product | Product category |
| Quantity | Number of units sold |
| Price | Price per unit |
| TotalSales | Quantity × Price |
| Store | Store location |
| Date | Transaction date |
| DayOfWeek | Day derived from date |
| Month | Month derived from date |

---

## 🛠️ Tools & Technologies
- **Azure Databricks**
- **Apache Spark (Databricks Runtime)**
- **Python**
- **Pandas & NumPy**
- **Matplotlib & Seaborn**
- **GitHub**

---

## 🧹 Data Processing & Feature Engineering
- Created a retail dataset using NumPy
- Converted raw data into Pandas DataFrame
- Derived new features:
  - `TotalSales`
  - `DayOfWeek`
  - `Month`
- Validated data types and integrity

---

## 📊 Exploratory Data Analysis (EDA)
Key EDA operations:
- Product-wise sales analysis
- Store-wise revenue comparison
- Customer spending behavior
- Time-based sales trends
- Distribution analysis of quantity and price

---

## 📈 Visualizations Performed
The following charts were created using Matplotlib & Seaborn:

- Bar Charts (Product & Store Sales)
- Line Charts (Daily & Monthly Trends)
- Pie & Donut Charts (Sales Contribution)
- Box & Violin Plots (Price & Quantity Distribution)
- Heatmap (Correlation Analysis)
- Stacked Bar Charts
- Bubble Charts (Price vs Sales vs Quantity)

---

## 🔍 Key Insights
- Identified **top-performing products** based on revenue
- Determined **highest revenue-generating stores**
- Found **peak sales periods**
- Analyzed **customer purchase patterns**
- Observed correlation between price, quantity, and sales

---

## 💼 Business Value
This analysis helps retail businesses:
- Optimize inventory management
- Improve store performance
- Identify high-value customers
- Make data-driven pricing decisions
- Enhance marketing strategies

---

## ▶️ How to Run the Project
1. Upload the dataset to **Azure Databricks**
2. Create a Databricks notebook
3. Load data using Pandas or Spark
4. Execute analysis and visualization cells
5. Interpret insights from charts and metrics

---

## 📌 Future Enhancements
- Real-time data ingestion
- Sales forecasting using ML models
- Customer segmentation
- Integration with Power BI dashboards
- Deployment using Azure Data Factory

---

## 👤 Author
**Ashwin Kumar**  
MBA in Data Analytics  
Aspiring Data Analyst | Azure Databricks | SQL | Python  

---

## ⭐ Conclusion
This project demonstrates practical implementation of **Retail Analytics in Azure Databricks**, combining data engineering, analytics, visualization, and business interpretation — making it a strong portfolio project for analytics roles.
