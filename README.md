# 🎓 Student Result Management System (SRMS)

A desktop-based **Student Result Management System** developed using **Python Tkinter** and **SQLite3**. The application helps educational institutions manage student records, courses, results, and reports efficiently through a user-friendly graphical interface.

---

## 📌 Project Overview

The Student Result Management System is designed to automate the process of managing student information and academic results. The system provides secure login and registration functionality, student record management, course management, result calculation, and report generation.

---

## ✨ Features

### 🔐 Authentication Module

* User Registration
* User Login
* Secure Access Control

### 👨‍🎓 Student Management

* Add New Student
* Update Student Details
* Delete Student Records
* Search Student by Roll Number
* View Student Information

### 📚 Course Management

* Add Course
* Update Course Details
* Delete Course
* View Available Courses

### 📝 Result Management

* Add Student Results
* Automatic Percentage Calculation
* Update Results
* Delete Results
* Search Results

### 📊 Report Module

* View Student Reports
* Display Academic Performance
* Generate Result Summary

### 🖥 Dashboard

* Total Students Counter
* Total Courses Counter
* Total Results Counter
* Analog Clock Display
* Easy Navigation Menu

---

## 🛠 Technologies Used

| Technology   | Purpose               |
| ------------ | --------------------- |
| Python       | Programming Language  |
| Tkinter      | GUI Development       |
| SQLite3      | Database Management   |
| Pillow (PIL) | Image Processing      |
| OOP Concepts | Application Structure |

---

## 📂 Project Structure

```text
Student_Result_Management_System/
│
├── login.py
├── register.py
├── dashboard.py
├── student.py
├── course.py
├── result.py
├── report.py
├── rms.db
│
├── images/
│   ├── logo_p.png
│   ├── bg.png
│   └── cl.jpg
│
└── README.md
```

---

## 🗄 Database Tables

### User Table

* id
* username
* password

### Student Table

* id
* roll
* name
* email
* gender
* dob
* contact
* admission
* course
* state
* city
* pin
* address

### Course Table

* id
* name
* duration
* charges
* description

### Result Table

* id
* roll
* name
* course
* marks
* full_marks
* percentage

---

## ⚙️ Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/student-result-management-system.git
```

### Step 2: Navigate to Project Folder

```bash
cd student-result-management-system
```

### Step 3: Install Dependencies

```bash
pip install pillow
```

### Step 4: Run Application

```bash
python login.py
```

---

## 📈 Result Calculation Formula

The percentage is calculated automatically using:

```text
Percentage = (Marks Obtained × 100) ÷ Full Marks
```

Example:

```text
Marks Obtained = 360
Full Marks = 500

Percentage = (360 × 100) / 500
Percentage = 72%
```

---

## 🔄 System Workflow

```text
User Login
      ↓
Dashboard
      ↓
Student Management
      ↓
Course Management
      ↓
Result Entry
      ↓
Result Calculation
      ↓
Report Generation
```

---

## 🎯 Objectives

* Reduce manual paperwork.
* Maintain student records efficiently.
* Generate accurate results automatically.
* Improve data security and accessibility.
* Provide a user-friendly interface.

---

## 🚀 Future Enhancements

* Web-Based Version using Flask/Django
* Student Login Portal
* PDF Report Generation
* Email Notifications
* Cloud Database Integration
* Mobile Application Support
* Online Result Publishing
* Advanced Search and Filtering

---

## 👨‍💻 Author

**Rohit Raj**

B.Tech (Computer Science & Engineering)

Project: Student Result Management System

---

## 📜 License

This project is developed for educational and academic purposes. Free to use and modify for learning purposes.

---

