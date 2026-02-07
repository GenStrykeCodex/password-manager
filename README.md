# Password Manager CLI

A clean, modular, and secure Command Line Interface (CLI) Password Manager built in Python. 
This project is a **refactored v2.0 rewrite** of an earlier single-file implementation, redesigned to demonstrate scalable architecture, separation of concerns, and structured data handling.

---

## Features

* Generate strong random passwords (8–32 characters)
* Store credentials using structured JSON storage
* Add new credentials (service, username, password)
* View all stored credentials
* View a single credential by service name
* Update existing credentials
* Delete credentials
* Modular architecture with clear responsibility layers

---

## 📁 Data Storage

Credentials are stored locally in a JSON file:

```json
{
  "gmail": {
    "service": "gmail",
    "username": "user@gmail.com",
    "password": "Ab@123",
    "created_at": "2026-02-06 19:45:00"
  }
}
```

* File is auto-created if missing
* Corrupted or malformed data is handled safely
* Storage location: `data/passwords.json`

---

## ▶ How to Run

1. Clone the repository
2. Navigate to the project root
3. Run:

```bash
python main.py
```

No external dependencies required (Python 3.9+ recommended).

---

## Project Structure

```
password-manager/
│
├── data/
│   └── passwords.json
│
├── models/
│   └── credential.py
│
├── services/
│   ├── credential_service.py
│   ├── password_service.py
│   └── storage_service.py
│
├── utils/
│   ├── file_handler.py
│   └── validators.py
│
├── main.py
├── README.md
├── CHANGELOG.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---
## Versioning

* `v1.0-legacy` – Original single-file implementation (archived)
* `v2.0.0` – Modular rewrite with JSON storage and clean architecture

---

## Future Improvements

* Master password authentication (hashed)
* Encrypted password storage
* Password masking in CLI
* Export credentials (CSV)
* Unit tests
* GUI version

---

## Author

Developed by [**GenStryke Codex**](https://github.com/GenStrykeCodex)

**LinkedIn**: <a href="https://linkedin.com/in/satyam-raj-anand" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="satyam raj anand" height="30" width="40" /></a>

**Instagram**: <a href="https://instagram.com/satyamraj_main.882" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="satyamraj_main.882" height="30" width="40" /></a>

---

## License

This project is licensed under the **MIT License**.

---
