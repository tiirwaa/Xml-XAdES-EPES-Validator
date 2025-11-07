<div align="center">
  <h1>Validador de Firma XAdES-EPES en Python</h1>
  <p>Valida firmas digitales XAdES-EPES en documentos XML, ideal para facturas electrónicas y otros documentos firmados digitalmente.</p>
</div>

---

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Salida esperada](#salida-esperada)
- [Generar ejecutable](#generar-ejecutable)
- [Notas](#notas)
- [Autor](#autor)

---

## Características

- Valida firmas XAdES-EPES en archivos XML.
- Detecta cualquier modificación en el XML firmado.
- Puede usarse como script de Python o ejecutable standalone.

## Requisitos

- Python 3.8 o superior
- Librerías Python:
  - `lxml`
  - `cryptography`
  - `pyopenssl`
  - `xmlsec`
  - `xades`

## Instalación

Instala las dependencias necesarias ejecutando:

```bash
pip install lxml cryptography pyopenssl xmlsec xades
```

## Uso

### Como script de Python

```bash
python validar_xades.py /ruta/al/archivo_firmado.xml
```

### Como ejecutable (Windows)

```bash
validar_xades.exe /ruta/al/archivo_firmado.xml
```

## Salida esperada

El script retorna:

- `True` si la firma es válida
- `False` si la firma NO es válida

Esto permite detectar si el XML ha sido modificado: cualquier alteración hará que la firma no sea válida.

## Generar ejecutable

Puedes generar un ejecutable con PyInstaller. Ejemplo de comando (ajusta la ruta de tu entorno Python):

```bash
python -m PyInstaller \
  --add-data ".../Python313/site-packages/xades/data;xades/data" \
  --add-data ".../Python313/site-packages/xmlsig/data;xmlsig/data" \
  validar_xades.py
```

Esto creará el ejecutable en la carpeta `dist/`.

## Notas

- Si tienes problemas con dependencias, revisa que `xmlsec` y `pyopenssl` estén correctamente instalados y configurados en tu sistema.
- El script está pensado para ser simple y portable.

---

## Autor

Andrey Rodriguez Araya