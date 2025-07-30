# SCT_SD_04
A python program that extracts product information, such as names, prices, and ratings, from an online e-commerce website and stores the data in a structured format like a CSV file.

---

# 🧠 SkillCraft Technology Internship - Task 04

## 📌 Task Objective

**Create a program that extracts product information, such as names, prices, and ratings, from an online e-commerce website and stores the data in a structured format like a CSV file.**

---

## ✅ Task Overview

This repository contains a Python script that automates data extraction from [Myntra](https://www.myntra.com) using **Selenium WebDriver**. The data collected includes:

- 🛍️ Product Name  
- 💰 Original Price  
- 🔻 Discounted Price  
- ⭐ Rating (if available)  
- 🔗 Product URL  
- 🖼️ Image URL  

The data is saved to a `.csv` file for further analysis or use.

---

## 🚀 How It Works

### 1. User is prompted to enter a search term:
```
🔍 Enter Myntra product search term (e.g., tops for women):
```

### 2. The script then:
- Launches Chrome
- Visits the search result pages
- Scrapes product data for up to 5 pages (can be modified)
- Stores results in a CSV file

---

## 🛠️ Setup Instructions

### 🔧 Prerequisites
- Python 3.x
- Google Chrome

### 📦 Install Required Packages
```bash
pip install selenium webdriver-manager
```

---

## ▶️ Run the Script

```bash
python task4.py
```

Then enter your product keyword, such as:

```
tops for women
```

A CSV file named `tops_for_women_myntra_products.csv` will be created with the extracted data.

---

## 🧾 Sample Output (CSV Columns)

| Name              | Original Price | Discounted Price | Rating | Product URL | Image URL |
|-------------------|----------------|------------------|--------|-------------|-----------|
| H&M Cotton Shirt  | ₹1299          | ₹699             | 4.3    | ...         | ...       |

---

## 🔍 Technologies Used

- Python 🐍  
- Selenium WebDriver 🌐  
- ChromeDriver via WebDriver Manager  
- CSV Module for structured output  

---

## 📸 Task Reference

<img width="1919" height="1011" alt="image" src="https://github.com/user-attachments/assets/9b52e1fa-d9b8-4215-9b16-166bc7573322" />


---

## 📄 License

This project is part of an internship assignment and is for educational use only.  
**© 2025 Meera Krishna ([@Meera-Krishna](https://github.com/Meera-Krishna))**


---
## 👩‍💻 Author

**Meera Krishna**  
_“⚙️ Debugging life one commit at a time — architecting logic, styling with sass, and deploying dreams.”_

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&style=flat-square)](https://www.linkedin.com/in/meera-krishna)

---
