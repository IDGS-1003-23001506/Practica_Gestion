import subprocess
import sys

def test_compra():
    # Ejecutar el script main.py y capturar la salida
    result = subprocess.run([sys.executable, 'main.py'], input='200\n25\n', text=True, capture_output=True)

    # Verificar que el código de salida sea 0 (éxito)
    assert result.returncode == 0

    # Verificar que la salida contenga los resultados esperados
    assert "Precio con descuento: 150.00" in result.stdout
    assert "Precio final con IVA: 174.00" in result.stdout