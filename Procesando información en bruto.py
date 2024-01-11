import requests

def descargar_y_guardar_csv(url, nombre_archivo):
    try:
        # Realizar el GET request
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa

        # Escribir la respuesta en un archivo CSV
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo_csv:
            archivo_csv.write(respuesta.text)

        print(f"Los datos han sido descargados y guardados en '{nombre_archivo}'.")
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

# URL de los datos
url_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"

# Nombre del archivo CSV
nombre_archivo_csv = "datos_moneda.csv"

# Llamar a la función
descargar_y_guardar_csv(url_datos, nombre_archivo_csv)
