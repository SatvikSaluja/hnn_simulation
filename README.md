# HNN-Core Integrity Suite

This repository contains a modular diagnostic tool for **HNN-Core** simulations. It separates the biophysical simulation logic from the regression testing framework to ensure model stability.

## Project Structure
* `hnn_simulate.py`: The production script that builds and runs the Jones 2009 model.
* `hnn_integrity.py`: The validation engine that audits peak latency and configuration integrity.

## Installation
```bash
pip install -r requirements.txt