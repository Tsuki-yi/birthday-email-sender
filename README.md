# 🎂 Birthday Email Sender

A Python project that automatically sends birthday greeting emails based on a local CSV file.

## 📌 Project Description

This script reads birthday information from a CSV file and checks whether anyone has a birthday today. If so, it sends a personalized birthday email using QQ Mail SMTP service.

This is my **first completed personal project after learning Python**, created as part of my preparation for Spring Insight Weeks and future technical roles (SDE) in the UK.

## 💡 Tech Stack

- Python 3.11
- `smtplib`, `email.mime`, `csv`, `datetime`
- Git + GitHub

## 📁 Project Structure
📦 birthday-email-sender
├── main.py              # Main script: date check + email logic
├── email_sender.py      # Encapsulated email-sending module
├── birthday_wisher.csv  # Birthday data (name, email, date)
├── test.py              # Test file
└── README.md
---

## 🚀 How to Use

1. Add birthday records into `birthday_wisher.csv` in the format:
name,email,birthday
Alice,alice@example.com,06-20
Bob,bob@example.com,12-25
2. Replace the sender email and password in `email_sender.py` with your own QQ Mail + App password.
3. Run `main.py`. If today matches any birthday in the CSV, it will send an email.

---

## 🧠 What I Learned

- How to structure a Python project
- How to work with date logic and CSV files
- How to send real emails via QQ SMTP (handling encoding issues)
- How to publish and manage projects on GitHub

---

## 👤 About Me

I'm an incoming Year 1 Engineering student at the University of Southampton. I'm passionate about technology and aiming to become a **Software Development Engineer (SDE)**.  
This project reflects my **initiative and commitment** to learning real-world development skills early.

> 🌱 I built this as part of my application portfolio for UK Spring Insight Weeks (Tech track).
