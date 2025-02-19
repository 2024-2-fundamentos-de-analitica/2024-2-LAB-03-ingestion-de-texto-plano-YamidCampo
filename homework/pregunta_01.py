"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd

def pregunta_01():
  """
  Construya y retorne un dataframe de Pandas a partir del archivo
  'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

  - El dataframe tiene la misma estructura que el archivo original.
  - Los nombres de las columnas deben ser en minusculas, reemplazando los
  espacios por guiones bajos.
  - Las palabras clave deben estar separadas por coma y con un solo
  espacio entre palabra y palabra.


  """

  with open('files/input/clusters_report.txt', 'r') as file:
        lines = file.readlines()

  indice = 4
  datos_lineas = lines[indice:]

  filas = []
  fila_actual = []

  for line in datos_lineas:
      if line.strip():
          fila_actual.append(line.strip())
      else:
          if fila_actual:
              filas.append(" ".join(fila_actual))
              fila_actual = []

  datos = []
  for fila in filas:
      piezas = fila.split()
      cluster = int(piezas[0])
      cantidad = int(piezas[1])
      porcentaje = float(piezas[2].replace(",", "."))
      palabras_clave = (
      " ".join(piezas[3:])
      .replace(" ,", ",")
      .replace(", ", ", ")
      .strip("%")
      .rstrip(".")
      .strip())
      datos.append([cluster, cantidad, porcentaje, palabras_clave])

  df = pd.DataFrame(datos, columns=[
      "cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"
  ])

  return df