# 🎓 Dynamic CGPA Calculator Suite

A versatile tool for students to calculate their Cumulative Grade Point Average (CGPA) with ease. This project offers two distinct versions: a **Desktop GUI** and a **Web-based Interface**.

---

## 🚀 Overview

This repository provides a flexible way to manage academic results. Instead of a fixed number of inputs, both versions allow you to dynamically add or remove subjects as needed.

### 🛠️ Platforms Included
1.  **Tkinter (Desktop):** A classic, lightweight Python application that runs natively on your computer.
2.  **Streamlit (Web):** A modern, responsive web application that runs in your browser.

---

## 📦 Installation & Setup

Ensure you have **Python 3.x** installed on your system.

### 1. Clone the Project
```bash
git clone [https://github.com/yourusername/cgpa-calculator.git](https://github.com/yourusername/cgpa-calculator.git)
cd cgpa-calculator
````

### 2\. Install Requirements

Tkinter is built into Python. However, Streamlit requires a quick installation:

```bash
pip install streamlit
```

-----

## 🖥️ Usage

### Running the Desktop App (Tkinter)

Simply run the Python script to open the window:

```bash
python tkinter_app.py
```

  * **Best for:** Quick, offline calculations.
  * **Key Feature:** Uses a class-based structure for efficient memory management.

### Running the Web App (Streamlit)

Launch the local server to view it in your browser:

```bash
streamlit run streamlit_app.py
```

  * **Best for:** A clean, modern UI and sharing with friends.
  * **Key Feature:** Auto-calculates as you type.

-----

## 📐 The Formula

Both apps calculate the CGPA based on the weighted average of credits:

$$CGPA = \frac{\sum (\text{Grade Points} \times \text{Credits})}{\sum \text{Total Credits}}$$

-----

## 💡 Features

  * **Add/Remove Rows:** No limit on the number of subjects.
  * **Error Handling:** Prevents crashes if text is entered instead of numbers.
  * **Responsive Layout:** The UI adjusts as you add more data.
  * **Visual Feedback:** Colorful status indicators for Pass/Fail or high CGPA scores.

-----
**Happy Studying\!** 📝

```

