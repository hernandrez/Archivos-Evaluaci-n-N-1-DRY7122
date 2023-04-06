# comprobar si hay un archivo
if [ $# -eq 0 ]
  then
    echo "Debe proporcionar un archivo como argumento."
    exit 1
fi

# Comprobar si el archivo existe
if [ ! -f "$1" ]
  then
    echo "El archivo proporcionado no existe."
    exit 1
fi

# Otorgar permiso de ejecución al archivo
chmod +x "$1"

# Cambiar la propiedad del archivo a root
sudo chown root "$1"

echo "El archivo se ha cambiado correctamente a propiedad de root y se ha concedido permiso de ejecución."

