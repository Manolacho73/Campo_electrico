import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl as op

import webbrowser as wb


q1 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
r = [100, 200, 300, 400, 100, 200, 300, 400, 100, 200, 300, 400,]

datos_tabla = {'Carga 1': q1, 'Distancia entre cargas': r}
df = pd.DataFrame(data=datos_tabla)

df['Campo Eléctrico'] = ((df['Carga 1'] * 2 * 9 * 10 * np.exp(9))/(df['Distancia entre cargas'] * np.exp(2))) 
print(df)

df.plot.line(x='Carga 1', y='Campo Eléctrico')

plt.show()

"""
# Actividad 
## Tomando como punto de partida el *ejemplo* del dibujo:
1. Intentá reproducirlo con el simulador PhET
2. Seleccioná una carga positiva de 1nC.
3. Seleccioná una segunda carga negativa de 1nC.
4. Seleccioná el ítem Campo Eléctrico.
5. Medí la distancia entre ambas cargas con la cinta métrica.
6. Medí la intensidad del Campo con el Voltímetro.
7. Utilizando la Grilla Cuadriculada, medí el módulo de los vectores.


"""
st.image('./Figuras/Ejemplo.jpg')

url = 'https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_es.html'

if st.button('Usar PhET de Campo Eléctrico'):
    wb.open_new_tab(url)
