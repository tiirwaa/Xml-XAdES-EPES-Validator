#!/usr/bin/env python3
import sys
import os
from lxml import etree
from xades import XAdESContext
from unittest.mock import patch

class UrllibMock:
    def read(self):
        return b""

def resource_path(relative_path):
    """Obtiene la ruta absoluta al recurso, compatible con PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def validar_firma_xades(xml_path):
    try:
        # Leer XML firmado
        with open(xml_path, "rb") as f:
            xml_data = f.read()
        xml_tree = etree.fromstring(xml_data)

        # Buscar nodo Signature en el namespace ds
        ns = {"ds": "http://www.w3.org/2000/09/xmldsig#"}
        signature_nodes = xml_tree.xpath("//ds:Signature", namespaces=ns)
        if not signature_nodes:
            raise Exception("No se encontró nodo Signature en el XML")
        signature_node = signature_nodes[0]

        # Cambiar directorio a la ruta base donde están las carpetas xades y xmlsig dentro del exe
        os.chdir(resource_path("."))

        # Crear contexto XAdES
        ctx = XAdESContext()

        # Parchear descarga remota de políticas para que no falle
        with patch("xades.policy.urllib.urlopen") as mock:
            mock.return_value = UrllibMock()
            # Validar la firma en el nodo Signature
            ctx.verify(signature_node)

        return True
    except Exception as e:
        print(f"Error validando firma XAdES: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <archivo_firmado.xml>", file=sys.stderr)
        sys.exit(1)

    archivo_xml = sys.argv[1]
    valido = validar_firma_xades(archivo_xml)
    print("true" if valido else "false")
    sys.exit(0 if valido else 1)
