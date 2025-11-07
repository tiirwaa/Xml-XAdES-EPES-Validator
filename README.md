For the Spanish version, see [README.es.md](README.es.md).

<div align="center">
  <h1>XAdES-EPES Signature Validator in Python</h1>
  <p>Validates XAdES-EPES digital signatures in XML documents, ideal for electronic invoices and other digitally signed documents.</p>
</div>

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Expected Output](#expected-output)
- [Generate Executable](#generate-executable)
- [Notes](#notes)
- [Author](#author)

---

## Features

- Validates XAdES-EPES signatures in XML files.
- Detects any modifications in the signed XML.
- Can be used as a Python script or standalone executable.

## Requirements

- Python 3.8 or higher
- Python libraries:
  - `lxml`
  - `cryptography`
  - `pyopenssl`
  - `xmlsec`
  - `xades`

## Installation

Install the necessary dependencies by running:

```bash
pip install lxml cryptography pyopenssl xmlsec xades
```

## Usage

### As a Python script

```bash
python validar_xades.py /path/to/signed_file.xml
```

### As an executable (Windows)

```bash
validar_xades.exe /path/to/signed_file.xml
```

## Expected Output

The script returns:

- `True` if the signature is valid
- `False` if the signature is NOT valid

This allows detecting if the XML has been modified: any alteration will make the signature invalid.

## Generate Executable

You can generate an executable with PyInstaller. Example command (adjust the path to your Python environment):

```bash
python -m PyInstaller \
  --add-data ".../Python313/site-packages/xades/data;xades/data" \
  --add-data ".../Python313/site-packages/xmlsig/data;xmlsig/data" \
  validar_xades.py
```

This will create the executable in the `dist/` folder.

## Notes

- If you have issues with dependencies, check that `xmlsec` and `pyopenssl` are correctly installed and configured on your system.
- The script is designed to be simple and portable.

---

## Author

Andrey Rodriguez Araya