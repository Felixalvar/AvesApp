"""Esta es una aplicación para identificar, por medio de filtros, aves de la zona del Baixo Miño. A medida que vamos
seleccionando filtros vamos cribando el número de aves hasta dar con la que nos interesa. Si no la encontramos podemos
limpiar los filtros y volver a empezar."""


# Importamos las librerías streamlit con su alias 'st', y pandas con el suyo 'pd'.

import streamlit as st
import pandas as pd

# A la pestaña de la página le damos un título, un icono y modificamos el diseño del área de la página ensanchándola
st.set_page_config(
    page_title='Buscador de Aves do Baixo Miño',
    # page_icon='🪶',
    page_icon=':owl:',
    layout='wide',
)

# Inicializamos todos los filtros de la barra lateral con una cadena vacía para que al iniciar la aplicación no dé
# ningún error.
nombreAve = tamanoAve = habitatAve = comportamientoAve = colorAve = patasColor = picoColor = picoForma = picoGrorsor = \
    picoLongitud = ""

# Creamos los checkbox de cada filtro de búsqueda en la barra lateral con sus opciones correspondientes y la
# primera vacía.
with st.sidebar:
    # Creamos la etiqueta subtítulo 'Filtro'
    st.subheader('Filtros:')
    # Creamos las casillas de verificación y sus opciones correspondientes. La primera opoción son todas las aves para
    # que si el usuario conoce el ave pueda elegirla e ir directamente a la ficha y foto de esa ave.
    if st.checkbox('Ave:'):
        nombreAve = st.selectbox('Elige un ave', ['',
                                                  'Abubilla',
                                                  'Acentor Común',
                                                  'Agachadiza Chica',
                                                  'Agachadiza Común',
                                                  'Águila Pescadora',
                                                  'Agateador Común',
                                                  'Aguja Colipinta',
                                                  'Alcatraz',
                                                  'Alcotán',
                                                  'Ánade Azulón',
                                                  'Andarríos Chico',
                                                  'Archibebe Claro',
                                                  'Arrendajo',
                                                  'Avión Común',
                                                  'Azor',
                                                  'Bisbita Común',
                                                  'Buitrón',
                                                  'Camachuelo Común',
                                                  'Carbonero Común',
                                                  'Carbonero Garrapinos',
                                                  'Carricerín Cejudo',
                                                  'Cernícalo Vulgar',
                                                  'Charrán Común',
                                                  'Charrán Patinegro',
                                                  'Chochín',
                                                  'Chorlitejo Grande',
                                                  'Chorlitejo Patinegro',
                                                  'Chorlito Gris',
                                                  'Chotacabras Gris',
                                                  'Cigüeña Blanca',
                                                  'Colirrojo Tizón',
                                                  'Cormorán Grande',
                                                  'Cormorán Moñudo',
                                                  'Corneja Negra',
                                                  'Correlimos Común',
                                                  'Correlimos Tridáctilo',
                                                  'Críalo',
                                                  'Cuco',
                                                  'Curruca Cabecinegra',
                                                  'Curruca Capirotada',
                                                  'Curruca Mosquitera',
                                                  'Curruca Rabilarga',
                                                  'Curruca Zarcera',
                                                  'Escribano Cerillo',
                                                  'Escribano Montesino',
                                                  'Escribano Palustre',
                                                  'Escribano Soteño',
                                                  'Espátula',
                                                  'Estornino Negro',
                                                  'Estornino Pinto',
                                                  'Faisán Vulgar',
                                                  'Focha Común',
                                                  'Fumarel Común',
                                                  'Garceta Común',
                                                  'Garceta Grande',
                                                  'Garza Real',
                                                  'Gavilán',
                                                  'Gaviota Argéntea',
                                                  'Gaviota Patiamarilla',
                                                  'Gaviota Reidora',
                                                  'Gaviota Sombría',
                                                  'Golondrina Común',
                                                  'Golondrina Daúrica',
                                                  'Gorrión Común',
                                                  'Gorrión Molinero',
                                                  'Halcón Abejero',
                                                  'Halcón Común',
                                                  'Herrerillo Capuchino',
                                                  'Herrerillo Común',
                                                  'Jilguero',
                                                  'Lavandera Blanca Común',
                                                  'Lavandera Boyera Ibérica',
                                                  'Lavandera Cascadeña',
                                                  'Lechuza Común',
                                                  'Lúgano',
                                                  'Martín Pescador',
                                                  'Milano Negro',
                                                  'Mirlo Común',
                                                  'Mito',
                                                  'Mochuelo Común',
                                                  'Mosquitero Común',
                                                  'Negrón Común',
                                                  'Ostrero',
                                                  'Paloma Torcaz',
                                                  'Papamoscas Cerrojillo',
                                                  'Perdiz Común',
                                                  'Petirrojo',
                                                  'Pico de Coral',
                                                  'Pico Menor',
                                                  'Pico Picapinos',
                                                  'Pinzón Vulgar',
                                                  'Pito Real',
                                                  'Polla de Agua',
                                                  'Ratonero Común',
                                                  'Reyezuelo Listado',
                                                  'Reyezuelo Sencillo',
                                                  'Tarabilla Común',
                                                  'Tórtola Común',
                                                  'Tórtola Turca',
                                                  'Urraca',
                                                  'Vencejo Común',
                                                  'Verdecillo',
                                                  'Verderón',
                                                  'Vuelvepiedras',
                                                  'Zarapito Trinador',
                                                  'Zarcero Común',
                                                  'Zorzal Común',
                                                  ])
  
    # Creamos las casillas de verificación y sus opciones correspondientes.
    if st.checkbox('Tamaño:'):
        tamanoAve = st.selectbox('Elije tamaño', ['',
                                                  'Más pequeño  que un gorrión',
                                                  'Como un gorrión',
                                                  'Entre un gorrión y un mirlo',
                                                  'Como un mirlo',
                                                  'Entre un mirlo y una paloma',
                                                  'Como una paloma',
                                                  'Entre una paloma y un pato',
                                                  'Como un pato',
                                                  'Más grande que un pato',
                                                  ])

    if st.checkbox('Hábitat'):
        habitatAve = st.selectbox('Elije hábitat', ['',
                                                    'Bosque/Árboles',
                                                    'Arbustos',
                                                    'Herbazales',
                                                    'Llanuras',
                                                    'Humedales',
                                                    'Urbanos',
                                                    'Cultivos',
                                                    'Costa',
                                                    'Ribera',
                                                    'Cortados/Acantilados',
                                                    ])

    if st.checkbox("Comportamiento"):
        comportamientoAve = st.selectbox('Elije comportamiento', ['',
                                                                  'En un bando o grupo',
                                                                  'Con otras aves',
                                                                  'Cazando/Pescando',
                                                                  'Inmóvil',
                                                                  'Caminando',
                                                                  'Saltando',
                                                                  'Moviendo la cola',
                                                                  'Picoteando en el suelo',
                                                                  'Posado en un oteadero',
                                                                  'Hurgando en el limo',
                                                                  'Buceando/Nadando',
                                                                  'Volando/Planeando',
                                                                  'Cerniéndose',
                                                                  ])

    if st.checkbox("Color"):
        colorAve = st.selectbox(
            'Elije color', ['',
                            'Blanco',
                            'Negro',
                            'Pío: blanco y negro',
                            'Gris',
                            'Crema',
                            'Naranja',
                            'Amarillo',
                            'Rojo',
                            'Verde',
                            'Azul',
                            'Marrón',
                            ])

    if st.checkbox("Patas color"):
        patasColor = st.selectbox(
            'Elije color patas', ['',
                                  'Blanco',
                                  'Negro',
                                  'Naranja',
                                  'Amarillo',
                                  'Rojo',
                                  'Verde',
                                  'Azul',
                                  'Marrón',
                                  'Rosa',
                                  'Gris',
                                  ])

    if st.checkbox("Pico color"):
        picoColor = st.selectbox(
            'Elije color pico', ['',
                                 'Blanco',
                                 'Negro',
                                 'Naranja',
                                 'Amarillo',
                                 'Rojo',
                                 'Verde',
                                 'Crema',
                                 'Marrón',
                                 'Rosa',
                                 'Gris',
                                 ])

    if st.checkbox("Pico forma"):
        picoForma = st.selectbox(
            'Elije forma pico', ['',
                                 'Ganchudo',
                                 'Curvado',
                                 'Puñal',
                                 'Pato',
                                 'Cónico',
                                 'Recto',
                                 ])

    if st.checkbox("Pico grosor"):
        picoGrorsor = st.selectbox(
            'Elije grosor pico', ['',
                                  'Fino',
                                  'Medio',
                                  'Grueso',
                                  ])

    if st.checkbox("Pico longitud"):
        picoLongitud = st.selectbox(
            'Elije longitud pico', ['',
                                    'Corto',
                                    'Medio',
                                    'Largo',
                                    ])

# Pomemos el título
st.title("_Buscador De Aves Do Baixo Miño_")

# Dividimos la página en dos columnas iguales
col1, col2 = st.columns([1, 1], gap="large")
# Podemos hacerla de igual tamaño de esta otra forma:
# col1, col2 = st.columns(2)

# Damos contenido a la columna de la izquierda donde irán las fichas de las aves seleccionadas.
with col1:
    # Situamos a los usuarios geográficamente mediante la imagen de un mapa con los concellos que forman O Baixo Miño.
    st.subheader('_Situación geográfica:_')
    st.image('./pythonProject/venv/AvesApp/Archivos/FotosDef/BaixoMino.png')
    st.caption("""**Espacio declarado Red Natura 2000 y Zona de Especial Protección para las Aves (ZEPA)**.
                  https://es.wikipedia.org/wiki/Red_Natura_2000""")
    # Recorremos el fichero .ods con pd.read_excel.
    df = pd.read_excel('./pythonProject/venv/AvesApp/Archivos/FichaAvesDefinitiva.ods', engine='odf', usecols='A:L')

    # Implementamos una excepción porque al cargar la página daba un NameError que al inicializar los filtros
    # como cadenas vacías ya no da. No obstante lo dejamos.
    try:
        # Vamos filtrando por cada etiqueta recogiendo la selección anterior
        df = df[df['Ave'].str.contains(nombreAve, case=False)]
        df = df[df['Tamaño'].str.contains(tamanoAve, case=False)]
        df = df[df['Hábitat'].str.contains(habitatAve, case=False)]
        df = df[df['Comportamiento'].str.contains(comportamientoAve, case=False)]
        df = df[df['Color'].str.contains(colorAve, case=False)]
        df = df[df['Patas color'].str.contains(patasColor, case=False)]
        df = df[df['Pico color'].str.contains(picoColor, case=False)]
        df = df[df['Pico forma'].str.contains(picoForma, case=False)]
        df = df[df['Pico grosor'].str.contains(picoGrorsor, case=False)]
        df = df[df['Pico longitud'].str.contains(picoLongitud, case=False)]

    except NameError:
        # Damos información al usuario
        st.subheader("Para iniciar la identificación hay que elegir algún filtro")

    # Convertimos el dfFichas en una lista que recorremos con for para mostrar las fichas de las aves seleccionadas con
    # cada filtro
    dfFichas = df.filter(items=['Ficha'])
    for valor in dfFichas.values.tolist():
        mifichero = open('./pythonProject/venv/AvesApp/Archivos/Fichas/' + valor[0], 'r', encoding='utf-8')
        texto = mifichero.read()
        mifichero.close()
        # Si no hay nada seleccionado no se muestra ninguna ficha y en caso contrario se muestran las
        # fichas de las aves seleccionadas
        if nombreAve == tamanoAve == habitatAve == comportamientoAve == colorAve == patasColor == picoColor == picoForma == \
                picoGrorsor == picoLongitud == "":
            pass
        else:
            st.subheader('_Ficha:_')
            st.caption(texto)

# En la colmna de la derecha mostraremos la/s foto/s del/de las ave/s filtrada/s, e informaremos como usar el buscador.
with col2:
    # INFORMACIÓN DEL FUNCIONAMIENTO DEL PROGRAMA
    # Indicamos un subtítulo
    st.subheader('_Uso del buscador:_')
    # Informamos de los pasos a seguir
    
    st.write("**_Si sabes qué ave es pincha en la casilla de verificación 'Ave' de la barra lateral y busca tu ave en "
             "el desplegable._**")
    st.write("**_Si no estás seguro sigue las siguientes instruciones:_**")
    st.write("**_1. Para iniciar la identificación hay que elegir algún filtro de la barra lateral, pinchar en la flecha "
             "del cuadro de selección y seleccionar una opción._**")
    st.write("**_2. Con cada filtro elegido vamos cribando el número de aves._**")
    st.write("**_3. Ve eligiendo el filtro que más te convenga._**")
    st.write("**_4. El orden de elección de los filtros no es importante._**")
    st.write("**_5. Si con los filtros elegidos no encuentras tu ave, puedes limpiar los filros y volver a empezar._**")
    st.write("**_6. Comienza cuando quieras._**")

    # Filtramos el dataframe por la columna Foto con los sucesivos filtros
    dfImagen = df.filter(items=['Foto'])

    # Sin no hay ningún ave seleccionada se le indica al usuario que con esos filtros no se localiza ningún ave
    if dfImagen.empty:
        st.subheader("_Con los filtros seleccionados no hay ningún ave en la base de datos._"
                     " _Inténtalo de nuevo._")
    else:
        pass

    # Convertimos el dfImagen en una lista que recorremos con for para mostrar las fotos de las aves seleccionadas con
    # cada filtro.
    for valor in dfImagen.values.tolist():
        # Si no hay nada seleccionado no se muestra ninguna foto y en caso contrario se muestran las fotos de las
        # aves seleccionadas
        if nombreAve == tamanoAve == habitatAve == comportamientoAve == colorAve == patasColor == picoColor == picoForma == \
                picoGrorsor == picoLongitud == "":
            pass
        else:
            st.subheader('_Foto:_')
            st.image('./pythonProject/venv/AvesApp/Archivos/FotosDef/' + valor[0] + '.png')
