# Password Manager CLI

**Project Status** : `STABLE RELEASE`

---

## v2.0.0 Changelog – Major Refactor & Clean Architecture

### Date : 07-02-2026

### Added

* Modular project structure (models, services, utils, ui)
* `Credential` data model with JSON serialization
* JSON-based credential storage (`passwords.json`)
* Safe file handling with automatic directory creation
* Password generation service with validation
* Centralized input validation utilities
* Full CRUD support for credentials
* Clean CLI menu system
* Defensive loading for malformed or corrupted data

### Changed

* Complete rewrite from single-file script to layered architecture
* Replaced plaintext `.txt` storage with structured JSON storage
* Reworked control flow to remove recursive menu calls
* Standardized service names as case-insensitive keys

### Removed

* Plaintext password storage in `.txt` files
* Inline input handling inside core logic
* Mixed UI and business logic

---

## v1.0-legacy Changelog – Initial Release

### Date: 21-07-2025

### Added

* Random password generation (8–32 characters)
* Plaintext password storage using `.txt` file
* Basic menu-driven CLI

### Known Limitations

* Single-file architecture
* No structured storage
* No edit or delete functionality
* No input validation
* Passwords stored in plain text

---
