# Validador de Firma XAdES-EPES en Python

Este proyecto contiene un script en Python para validar firmas digitales XAdES-EPES en documentos XML, especialmente para documentos electrónicos como facturas firmadas.

---

## Requisitos

- Python 3.8 o superior
- Librerías Python:
  - `lxml`
  - `cryptography`
  - `pyopenssl`
  - `xmlsec`
  - `xades`

### Instalación rápida de dependencias

```bash
pip install lxml cryptography pyopenssl xmlsec xades

### USO

python3 validar_xades.py /ruta/al/archivo_firmado.xml
---
validar_xades.exe /ruta/al/archivo_firmado.xml

Retorna: True si la firma es válida, False si no es válida. (Permite detectar si el xml sufrió modificaciones, cualquier modificación hara que la firma no sea válida.)

### GENERAR EJECUTABLE
 python -m PyInstaller --add-data ".../Python313/site-packages/xades/data;xades/data" --add-data ".../Python313/site-packages/xmlsig/data;xmlsig/data" validar_xades.py

###
Autor: Andrey Rodriguez