import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl as op

import webbrowser as wb

tab1, tab2, tab3 = st.tabs(['Tabla Teórica', 'Actividad 1', 'Actividad 2'])
with tab1:
    st.write('## Tabla Ejemplo')
    q1 = [1 , 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    r = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

    datos_tabla = {'Carga 1 (nC)': q1, 'Distancia entre cargas (m)': r}
    df = pd.DataFrame(data=datos_tabla)

    df['Campo Eléctrico'] = ((df['Carga 1 (nC)'] * 10 **(-9) * 9 * 10 **(9))/(df['Distancia entre cargas (m)'] **(2))) 
    print(df)

    st.dataframe(df)
    st.bar_chart(data=df, x='Carga 1 (nC)', y='Campo Eléctrico')
    
with tab2:
    """
    # Actividad 1
    ## Tomando como punto de partida el *ejemplo* del dibujo:
    1. Intentá reproducirlo con el simulador PhET
    2. Seleccioná una carga positiva de 1nC.
    3. Seleccioná una segunda carga negativa de 1nC.
    4. Seleccioná el ítem Campo Eléctrico.
    5. Medí la distancia entre ambas cargas con la cinta métrica.
    6. Medí la intensidad del Campo con el Voltímetro.
    7. Utilizando la Grilla Cuadriculada, medí el módulo de los vectores.
    8. Calculá el Campo Eléctrico usando la Ecuación a continuación.

    """
    st.image('./Figuras/ejemplo2.png')

    """
        # Campo Eléctrico generado por una carga puntual           

        $ E = \cfrac{k*q}{r^2} $

        * $ E $ : Campo eléctrico 
        * $ q $ : Carga (en $ \C (coulombios) $)
        * $ r $ : Distancia entre cargas eléctricas (en $ \m (metros) $)
        * $ k $ : Constante eléctrica del medio (su valor es $ \ 9*10^{9} N*m^2*C^{-2} $)
        
    """

    url = 'https://phet.colorado.edu/sims/html/charges-and-fields/latest/charges-and-fields_es.html'

    if st.button('Usar PhET de Campo Eléctrico'):
        wb.open_new_tab(url)
with tab3:
    """
    # Actividad 2
    ## Usando el Simulador PhET:
    1. Seleccioná una carga positiva.
    2. Ingresala con el botón *carga*.
    3. Seleccioná una segunda carga negativa de 1nC.
    4. Seleccioná el ítem Campo Eléctrico.
    5. Medí la distancia entre ambas cargas con la cinta métrica.
    6. Ingresala con el botón *distancia*.
    6. Medí la intensidad del Campo con el Voltímetro.
    7. Utilizando la Grilla Cuadriculada, medí el módulo de los vectores.
    8. Calculá el Campo Eléctrico usando la aplicación *Ecuación*.

    """
    col1, col2 = st.columns(2)
    with col1:
        carga = st.number_input('Inserte el valor de carga (nC)', min_value=0., max_value=10., step=.1, format='%.1f')
        st.write(f'El valor insertado es {carga: .1f}')

    with col2:
        distancia = st.number_input('Inserte el valor de distancia (m)', min_value=0., max_value=10., step=.1, format='%.1f')
        st.write(f'El valor insertado es {distancia: .1f}')
    
    r = st.number_input('distancia', 0, 100, 50, 1)
    x = np.linspace(0, 200, 300)
    y = 9 * 10 **(9) * x / r**2
    
    f = plt.figure()
    plt.plot(x, y, lw=2, c='r')
    f
    