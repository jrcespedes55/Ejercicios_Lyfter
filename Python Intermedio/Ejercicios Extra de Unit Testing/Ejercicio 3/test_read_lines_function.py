import pytest
from unittest.mock import patch, mock_open
from read_lines_function import read_lines 

def test_read_lines_success():
    # 1. Definimos el contenido simulado del archivo
    fake_file_content = "Línea 1\nLínea 2\nLínea 3"
    
    # 2. Creamos el mock de open con ese contenido
    mock = mock_open(read_data=fake_file_content)
    
    # 3. Reemplazamos temporalmente la función 'open' integrada de Python
    with patch("builtins.open", mock):
        resultado = read_lines("ruta/falsa/archivo.txt")
    
    # 4. Verificaciones (Assertions)
    assert resultado == ["Línea 1\n", "Línea 2\n", "Línea 3"]
    mock.assert_called_once_with("ruta/falsa/archivo.txt", "r")


def test_read_lines_file_not_found():
    # Simulamos que 'open' lanza la excepción FileNotFoundError al ser llamada
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            read_lines("archivo_que_no_existe.txt")
