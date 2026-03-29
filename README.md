# HNN Validation & Integrity Framework

A modular diagnostic and validation tool for **HNN-Core** simulations, designed to improve reliability and detect inconsistencies in simulation outputs.

This project separates **simulation execution** from **validation logic**, enabling clearer testing workflows and better maintainability.


<img width="1109" height="587" alt="image" src="https://github.com/user-attachments/assets/deb24911-3a39-4901-a5db-0d2d8b504314" />



## Project Structure
* `hnn_simulate.py`: Builds and runs the Jones 2009 neural model to generate simulation outputs.
* `hnn_integrity.py`: Validates simulation outputs by auditing peak latency and configuration consistency.

## Workflow
Run simulation → Generate outputs → Apply validation checks → Detect inconsistencies

## Installation & Usage
```bash
# Installation
pip install -r requirements.txt

# Usage
python hnn_simulate.py
python hnn_integrity.py
