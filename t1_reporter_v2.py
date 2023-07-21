import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import textwrap

st.set_page_config(page_title="T1 Reporteador Mejoredu", page_icon=":bar_chart:", layout='centered', initial_sidebar_state='auto')

password = st.text_input("Ingrese la contraseña", type="password")

if password == 't1mejoredu2023':

    # Carga los datos de un reactivo específico de una figura específica
    def cargar_datos_reactivo(figura, reactivo):
        # Nombre del archivo csv
        archivo_csv = f'{figura}_{reactivo}.csv'
        df = pd.read_csv(archivo_csv, index_col='Variable')
        return df

    # Diccionarios de escalas e incisos
    escalas_dict = {
        "b1": ["Mucho", "Regular", "Poco", "Nada"],
        "b2": ["Mucho", "Regular", "Poco", "Nada"],
        "b3": ["Totalmente de acuerdo", "De acuerdo", "En desacuerdo", "Totalmente en desacuerdo"],
        "b4": ["Muy pertinente", "Pertinente", "Poco pertinente", "Nada pertinente"],
        "b5": ["Muy adecuado", "Adecuado", "Poco adecuado", "Nada adecuado"],
        "b6": ["Totalmente de acuerdo", "De acuerdo", "En desacuerdo", "Totalmente en desacuerdo", "No sé o no estoy seguro"],
        "c1": ["Totalmente de acuerdo", "De acuerdo", "En desacuerdo", "Totalmente en desacuerdo"],
        "c2": ["Muy adecuado", "Adecuado", "Poco adecuado", "Nada adecuado"],
        "c3": ["Formar parte de alguna red de docentes/directores", "Recibir asesoría y acompañamiento por parte de la supervisión o de un asesor técnico pedagógico", "Participar en ejercicios colectivos de reflexión y análisis sobre el plan de estudio en la escuela", "Participar en programas de especialización de métodos de enseñanza colectivos", "Acceder a cursos o talleres relacionados con las características del plan de estudio", "Participar en ejercicios colectivos de reflexión y análisis sobre el plan de estudio a nivel de zona o sector escolar"],
        "d1": ["Sí", "No"],
        "d2": ["Sí", "No"],
        "e1": ["Siempre","Muchas veces","Pocas veces","Nunca"],
        "e2": ["Sí", "No"],
        "g1": ["Sí", "No", "No aplica"],
        "g2": ["Muy difícil", "Difícil", "Poco difícil", "Nada difícil"]

        # Agrega más entradas aquí según sea necesario.
    }

    incisos_dict = {
        "b1": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
        "b2": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
        "b3": ["A", "B", "C", "D", "E"],
        "b4": ["A", "B", "C", "D", "E", "F", "G"],
        "b5": ["A", "B", "C", "D", "E", "F"],
        "b6": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
        "c1": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
        "c2": ["A", "B", "C", "D", "E", "F", "G", "H"],
        "c3": ["A", "B", "C", "D", "E", "F"],
        "d1": ["A", "B", "C", "D", "E", "F", "G"],
        "d2": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
        "e1": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"],
        "e2": ["A", "B", "C", "D", "E", "F"],
        "g1": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
        "g2": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"],

        # Agrega más entradas aquí según sea necesario.
    }


    figuras = {
        'doc_pre': 'Docentes de preescolar',
        'doc_pri': 'Docentes de primaria',
        'doc_sec': 'Docentes de secundaria',
        'dir': 'Directores',
    }

    reactivos = {
        'b1': 'B1.¿Qué tan familiarizado está con los siguientes conceptos o acciones que sustentan el Plan de Estudio 2022?',
        'b2': 'B2. ¿Qué tan familiarizado está con los siguientes elementos que componen el Plan de Estudio 2022 y sus características?',
        'b3': 'B3. ¿Qué tan de acuerdo o en desacuerdo está en que las siguientes afirmaciones corresponden a las finalidades de los ejes articuladores?',
        'b4': 'B4. ¿Qué tan pertinentes considera son los siguientes elementos del programa sintético para elaborar los programas analíticos?',
        'b5': 'B5. ¿Qué tan adecuadas considera las siguientes características del programa analítico?',
        'b6': 'B6. ¿Qué tan de acuerdo o en desacuerdo está con las siguientes afirmaciones relacionadas con el Plan de Estudio 2022?',
        'c1': 'C1. ¿Qué tan de acuerdo está en que las siguientes habilidades docentes requieren fortalecerse para favorecer la apropiación del Plan de Estudio 2022?',
        'c2': 'C2. ¿Qué tan adecuadas han sido las siguientes acciones para que los docentes de su escuela se apropien del Plan de Estudio 2022?',
        'c3': 'C3. Con base en su opinión, ¿qué tan importantes considera las siguientes acciones de formación para favorecer la apropiación del Plan de Estudio 2022?',
        'd1': 'D1. ¿Cuáles de los siguientes retos han enfrentado los docentes de su escuela para la elaboración de los programas analíticos?',
        'd2': 'D2. Señale si recurrió o no a los siguientes materiales o recursos para trabajar en el diseño del programa analítico en su escuela',
        'e1': 'E1. ¿Con qué frecuencia se presentan las siguientes situaciones al trabajar con el colectivo docente en el marco de la elaboración de los programas analíticos?',
        'e2': 'E2. ¿Con cuáles de los siguientes recursos o apoyos cuentan en su escuela para elaborar los programas analíticos de forma colectiva?',
        'g1': 'G1. ¿Cuáles de los siguientes actores educativos considera conveniente que participen en la puesta en marcha del Plan de Estudio 2022?',
        'g2': 'G2. ¿Qué grado de dificultad considera pudieran tener las siguientes acciones al momento de poner en marcha los programas analíticos en el aula?'

    }

    st.markdown(
        """
        <style>
        .big-font {
            font-size:20px !important;
            font-family: Montserrat;
            color: white;
        }
        .title-container {
            background-color: #507E32;
            padding: 10px;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="title-container">
            <p class="big-font">Reporte de estudio de seguimiento a los procesos de conocimiento y apropiación del plan y programas de estudio 2022</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    figura_seleccionada = st.sidebar.selectbox('Seleccione la figura educativa:', list(figuras.keys()), format_func=lambda x: figuras[x])
    reactivo_seleccionado = st.sidebar.selectbox('Seleccione el reactivo:', list(reactivos.keys()), format_func=lambda x: reactivos[x])

    df = cargar_datos_reactivo(figura_seleccionada, reactivo_seleccionado)

    # Obtener las etiquetas de los incisos para el reactivo seleccionado
    reactivo_inciso_etiquetas = {
        'b1': {
            'Inciso A': 'a. La didáctica recupera los saberes ancestrales de las comunidades',
            'Inciso B': 'b. Se promueve el pensamiento crítico y reflexivo',
            'Inciso C': 'c. Se consideran metodologías socio-críticas para el abordaje de los campos formativos',
            'Inciso D': 'd. Se promueve la evaluación formativa de los aprendizajes',
            'Inciso E': 'e. Se coloca a la comunidad como el núcleo integrador de los procesos de enseñanza y aprendizaje',
            'Inciso F': 'f. Se impulsa la autonomía profesional docente para contextualizar los contenidos del currículo',
            'Inciso G': 'g. Se promueve una educación que reconoce a niñas, niños y adolescentes como sujetos de la educación',
            'Inciso H': 'h. Se impulsa una educación para una ciudadanía democrática',
            'Inciso I': 'i. Se reconoce el papel de las familias en la educación de las niñas, niños y adolescentes',
        },
        'b2': {
            'Inciso A': 'a. El currículo se organiza en cuatro campos formativos',
            'Inciso B': 'b. El currículo se organiza en fases de aprendizaje que se componen de grados escolares',
            'Inciso C': 'c. El currículo cuenta con siete ejes articuladores transversales a los campos formativos',
            'Inciso D': 'd. Las fases de aprendizaje posibilitan que los estudiantes consoliden nuevos saberes',
            'Inciso E': 'e. Los contenidos se articulan con situaciones que son relevantes para el sujeto y la comunidad',
            'Inciso F': 'f. Los rasgos globales del aprendizaje ofrecen una visión integral de lo que los estudiantes habrán de desarrollar',
        },
        'b3': {
            'Inciso A': 'a. Refieren a temáticas de relevancia social',
            'Inciso B': 'b. Permiten conectar los contenidos de diferentes disciplinas dentro de un campo formativo',
            'Inciso C': 'c. Permiten vincular las acciones de enseñanza y aprendizaje con la realidad de los estudiantes',
            'Inciso D': 'd. Propician un conjunto de saberes que le dan significado a los contenidos aprendidos',
            'Inciso E': 'e. La forma en que se articulan con los contenidos la deciden los docentes',
        },
        'b4': {
            'Inciso A': 'a. La organización por campos formativos',
            'Inciso B': 'b. La articulación entre campos formativos',
            'Inciso C': 'c. Los procesos de desarrollo por grado o grupo de edad considerados en su estructura',
            'Inciso D': 'd. Las sugerencias de evaluación propuestas',
            'Inciso E': 'e. Los insumos para organizar la planeación didáctica',
            'Inciso F': 'f. Las orientaciones para la puesta en marcha de las actividades',
            'Inciso G': 'g. Las fuentes de consulta para localizar materiales de apoyo para el diseño de las actividades'
        },
        'b5': {
            'Inciso A': 'a. La incorporación de contenidos locales',
            'Inciso B': 'b. La incorporación de los ejes articuladores',
            'Inciso C': 'c. Tomar en cuenta el diagnóstico de las problemáticas y características de la comunidad',
            'Inciso D': 'd. La posibilidad de articular conocimientos de distintos campos formativos',
            'Inciso E': 'e.La flexibilidad para organizar los contenidos según el criterio del maestro'
        },
        'b6': {
            'Inciso A': 'a. Existe mayor congruencia en las formas de trabajo entre los niveles educativos de preescolar, primaria y secundaria',
            'Inciso B': 'b. El trabajo por proyectos es una oportunidad para realizar una evaluación formativa',
            'Inciso C': 'c. El trabajo por proyectos es una oportunidad para trabajar en colectivo',
            'Inciso D': 'd. En el trabajo por proyectos el estudiante tiene un papel activo en su aprendizaje',
            'Inciso E': 'e. Los métodos sociocríticos promueven el aprovechamiento del potencial de los estudiantes',
            'Inciso F': 'f. La práctica docente necesita renovarse]',
            'Inciso G': 'g. La reflexión sobre la práctica docente es necesaria',
            'Inciso H': 'h.Los contenidos se aprenderán con mayor facilidad al articularse con situaciones locales',
            'Inciso I': 'i.La organización de grados en fases hace explícita la consolidación de los aprendizajes'
        },
        'c1': {
            'Inciso A': 'a. Reflexionar sobre la práctica docente',
            'Inciso B': 'b. Trabajar colaborativamente con la comunidad escolar',
            'Inciso C': 'c. Diseñar estrategias de evaluación formativa',
            'Inciso D': 'd. Implementar métodos de enseñanza colectivos',
            'Inciso E': 'e. Identificar necesidades, características y el contexto de la comunidad',
            'Inciso F': 'f. Emplear metodologías socio-críticas de enseñanza',
            'Inciso G': 'g. Implementar proyectos integradores para el aprendizaje',
            'Inciso H': 'h. Incorporar los ejes articuladores en las actividades de aprendizaje',
            'Inciso I': 'i.Implementar actividades para establecer vínculos pedagógicos en los tres escenarios (aula, escuela y comunidad)'
        },
        'c2': {
            'Inciso A': 'a.  Analizar las características y fundamentos que sustentan el marco curricular',
            'Inciso B': 'b.  Recuperar la información que surgió de la reflexión del colectivo docente',
            'Inciso C': 'c.  Recibir acompañamiento y asesoría de autoridades escolares',
            'Inciso D': 'd.  Consultar materiales de apoyo',
            'Inciso E': 'e.  Recibir retroalimentación para mejorar las acciones implementadas',
            'Inciso F': 'f.  Participar con el colectivo docente en las sesiones del CTE intensivo',
            'Inciso G': 'g.  Realizar actividades para profundizar en los conocimientos sobre el plan de estudio',
            'Inciso H': 'h.  Participar en discusiones para la incorporación de contenidos locales en los programas de estudio'
        },
        'c3': {
            'Inciso A': 'Primer lugar en importancia',
            'Inciso B': 'Segundo lugar en importancia',
            'Inciso C': 'Tercer lugar en importancia',
            'Inciso D': 'Cuarto lugar en importancia',
            'Inciso E': 'Quinto lugar en importancia',
            'Inciso F': 'Sexto lugar en importancia'
        },
        'd1': {
            'Inciso A': 'a. Conocimiento de las características (físicas, geográficas, culturales, entre otras) de la localidad',
            'Inciso B': 'b. Identificación de las necesidades, intereses, características sociales, económicas y familiares de la comunidad escolar',
            'Inciso C': 'c. Escucha y recuperación de las voces de la comunidad escolar',
            'Inciso D': 'd. Deliberación de los contenidos que se integrarán en los programas analíticos',
            'Inciso E': 'e. Incorporación de temáticas relevantes para la comunidad en los contenidos curriculares',
            'Inciso F': 'f. Diseñar actividades con base en las problemáticas de la localidad',
            'Inciso G': 'g. Articular los campos formativos en actividades integradoras',

        },
        'd2': {
            'Inciso A': 'a. Videos disponibles en la página de la SEP',
            'Inciso B': 'b. Acuerdo número 14/08/22 por el que se establece el Plan de Estudio para la educación preescolar, primaria y secundaria',
            'Inciso C': 'c. Anexo del Acuerdo número 14/08/22 por el que se establece el Plan de Estudio para la educación preescolar, primaria y secundaria',
            'Inciso D': 'd. Avance del contenido para el libro del docente. El diseño creativo',
            'Inciso E': 'e. Avance del contenido del programa sintético',
            'Inciso F': 'f. Guía del Taller Intensivo de Formación Continua para docentes',
            'Inciso G': 'g. Material de la metodología basada en proyectos, basada en problemas y STEAM',
            'Inciso H': 'h. Material para trabajar en procesos de aprendizaje y servicio a la comunidad en un mismo proyecto',
            'Inciso I': 'i. Presentaciones oficiales sobre el Plan de Estudio 2022',

        },
        'e1': {
            'Inciso A': 'a. Existe la disposición para trabajar en equipo',
            'Inciso B': 'b. Las interacciones son respetuosas y cordiales',
            'Inciso C': 'c. Hay grupos de docentes que no se llevan bien',
            'Inciso D': 'd. Se comparten experiencias sobre la práctica pedagógica',
            'Inciso E': 'e. Se definen metas en común',
            'Inciso F': 'f. Un grupo o persona impone sus ideas sobre los demás',
            'Inciso G': 'g. Se resuelven los conflictos o discrepancias escuchando argumentos y dialogando',
            'Inciso H': 'h. Prevalece una actitud positiva hacia las propuestas de cambio',
            'Inciso I': 'i. Se reconoce que se requiere la innovación de la práctica docente',
            'Inciso J': 'j. Existe disposición para resolver en conjunto los problemas que surgen con los estudiantes',
            'Inciso K': 'k. La retroalimentación ocurre en un clima de confianza'
        },
        'e2': {
            'Inciso A': 'a. Asesoría y acompañamiento por parte del personal directivo',
            'Inciso B': 'b. Apoyo de la supervisión',
            'Inciso C': 'c. Tiempo laboral para poder reunirse',
            'Inciso D': 'd. Espacios físicos para llevar a cabo las reuniones',
            'Inciso E': 'e. Acceso a Internet',
            'Inciso F': 'f. Equipamiento tecnológico',
        },
        'g1': {
            'Inciso A': 'a. Colectivo docente',
            'Inciso B': 'b. Director',
            'Inciso C': 'c. Supervisor',
            'Inciso D': 'd. Subdirectores (académico o de gestión)',
            'Inciso E': 'e. Asesor técnico pedagógico',
            'Inciso F': 'f. Padres de familia',
            'Inciso G': 'g. Autoridades estatales',
            'Inciso H': 'h. Autoridades locales',
            'Inciso I': 'i. Autoridades comunitarias',
        },
        'g2': {
            'Inciso A': 'a. Diseñar actividades para el aprendizaje basado en proyectos',
            'Inciso B': 'b. Trabajar en colectivo para diseñar proyectos contemplando varios campos formativos',
            'Inciso C': 'c. Involucrar a los padres de familia y a la comunidad en el aprendizaje de los estudiantes',
            'Inciso D': 'd. Lograr que los estudiantes se involucren en las actividades integradoras de los contenidos',
            'Inciso E': 'e. Disponer de los recursos para la implementación de los proyectos',
            'Inciso F': 'f. Diseñar materiales didácticos para realizar las actividades integradoras de los contenidos',
            'Inciso G': 'g. Enfrentar situaciones emergentes para el desarrollo de las actividades de aprendizaje',
            'Inciso H': 'h. Disponer de tiempos para llevar a cabo los proyectos',
            'Inciso I': 'i. Implementar proyectos que favorezcan la transversalidad de los contenidos',
            'Inciso J': 'j. Comprender los conceptos clave del Plan de Estudio 2022',
            'Inciso K': 'k. Apropiarse de la orientación pedagógica que propone el Plan de Estudio 2022'
        }

    }

    # Verificar si el reactivo seleccionado tiene etiquetas de incisos definidas
    if reactivo_seleccionado in reactivo_inciso_etiquetas:
        inciso_etiquetas = reactivo_inciso_etiquetas[reactivo_seleccionado]
    else:
        inciso_etiquetas = {}


    # Aquí definimos las categorías y sus posibles valores
    categorias = {
        'Entidad': ['AGUASCALIENTES', 'BAJA CALIFORNIA', "BAJA CALIFORNIA SUR", "CAMPECHE", "CHIAPAS", "CHIHUAHUA", "CIUDAD DE MÉXICO", "COAHUILA", "COLIMA", "DURANGO", "ESTADO DE MÉXICO", "GUANAJUATO", "GUERRERO", "HIDALGO", "JALISCO", "MICHOACÁN", "MORELOS", "NAYARIT", "NUEVO LEÓN", "PUEBLA", "QUERÉTARO", "QUINTANA ROO", "SAN LUIS POTOSÍ", "SINALOA", "SONORA", "TABASCO", "TAMAULIPAS", "TLAXCALA", "VERACRUZ", "YUCATÁN", "ZACATECAS"],  
        'Sexo': ['Hombre', 'Mujer', 'Total'],
        'Rangos de edad': ["18 a 20 años", "21 a 30 años", "31 a 40 años", "41 a 50 años", "51 a 60 años", "61 a 70 años", "71 a 80 años", "81 a 90 años", "91 a 99 años", "Total"],
        'Estudios': ["Preparatoria, bachillerato o carrera técnica", "Normal básica sin licenciatura", "Normal superior", "Normal Intercultural Bilingüe", "Licenciatura", "Especialidad", "Maestría", "Doctorado", "Posdoctorado", "Total"],
        'Experiencia laboral': ['Menor o igual a 10', '11 a 20', "21 a 30", "31 a 40", "41 a 50", "Mayor o igual a 51", "Total"],
        'Tipo de nombramiento': ['Definitivo o base', 'Interino', "No tengo nombramiento", "Otro", "Total"]
    }

    categoria1 = st.sidebar.selectbox('Seleccione el dato de identificación:', list(categorias.keys()))

    # Deducir los incisos únicos a partir del diccionario
    incisos = incisos_dict[reactivo_seleccionado]

    inciso_etiquetas_list = list(inciso_etiquetas.values())
    inciso_etiquetas_list.insert(0, '')

    inciso_seleccionado_index = st.sidebar.selectbox('Seleccione el inciso del reactivo:', range(1, len(inciso_etiquetas_list)), format_func=lambda x: inciso_etiquetas_list[x])


    if inciso_seleccionado_index > 0:
        inciso_seleccionado = incisos[inciso_seleccionado_index - 1]
    else:
        inciso_seleccionado = ''

    subconjunto_df = df.loc[categorias[categoria1]]
    # Configurar el nombre del índice
    subconjunto_df.index.name = categoria1
    subconjunto_df = subconjunto_df.fillna(0)

    # Filtrar por las columnas que corresponden al inciso seleccionado y a la escala del reactivo
    columnas_seleccionadas = []
    for escala in escalas_dict[reactivo_seleccionado]:
        columnas_seleccionadas.extend(subconjunto_df.columns[subconjunto_df.columns.str.contains(f'^B\d-{inciso_seleccionado}-{escala}-% del N de fila$')])

    subconjunto_df = subconjunto_df[columnas_seleccionadas]

    # Convierte los datos a porcentajes
    subconjunto_df = subconjunto_df.apply(pd.to_numeric, errors='coerce')
    subconjunto_df *= 100
    # Formatea los datos a string y añade el símbolo de porcentaje
    subconjunto_df = subconjunto_df.applymap('{:.0f}%'.format)
    
    # Si se quiere mostrar el dataframe original, solo hay que descomentar la línea de abajo:

    #st.write(subconjunto_df)

    # Convierte los datos a formato numérico de nuevo para el gráfico
    subconjunto_df = subconjunto_df.applymap(lambda x: float(x.strip('%')))

    # Gráfica

    # Concatenar selecciones de cajas de selección
    max_title_length = 200
    reactivo = reactivos[reactivo_seleccionado]
    if len(reactivo) > max_title_length:
        reactivo = reactivo[:max_title_length] + '...'

    # Define cuántos caracteres quieres por línea
    caracteres_por_linea = 74

    # Obtiene la figura seleccionada
    figura_etiqueta = figuras[figura_seleccionada]

    # Divide el reactivo en líneas
    lineas = textwrap.wrap(reactivo, caracteres_por_linea)

    # Une las líneas con el carácter de nueva línea
    reactivo = '\n'.join(lineas)

    # Obtén la etiqueta del inciso seleccionado desde el índice seleccionado en la caja
    inciso_etiqueta = inciso_etiquetas_list[inciso_seleccionado_index]

    # Incluye la figura seleccionada y la etiqueta del inciso en el título
    titulo_grafico = f"{figura_etiqueta}\n{reactivo}\n{inciso_etiqueta}"



    # Crear un nuevo DataFrame basado en el original
    nuevo_df = subconjunto_df.copy()

    # Renombrar encabezados para mostrar solo la escala de respuesta
    nuevo_df.columns = [col.split('-')[2] for col in nuevo_df.columns]
    
    # Convertir los datos a formato de cadena y agregar el signo de porcentaje
    nuevo_df = nuevo_df.applymap(lambda x: f'{x:.0f}%')

    # Muestra el título antes del DataFrame
    st.markdown(f'<div style="font-size:16px"><b>{titulo_grafico}</b></div>', unsafe_allow_html=True)

    # Muestra el nuevo DataFrame
    st.write(nuevo_df)


    # Crea la gráfica de barras apiladas
    colores = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8B00FF"]

    if 'Total' in subconjunto_df.index:
        ax = subconjunto_df.drop('Total', axis=0).plot(kind='bar', stacked=True, color=colores)
    else:
        ax = subconjunto_df.plot(kind='bar', stacked=True, color=colores)

    # Restaura los valores de porcentaje en el eje y de la gráfica
    ax.yaxis.set_major_formatter(lambda x, _: '{:.0f}%'.format(x))

    # Restaura las etiquetas de porcentaje en las barras de la gráfica
    show_labels = st.sidebar.checkbox('Mostrar valores (%) en el gráfico')
    if show_labels:
        for p in ax.patches:
            width, height = p.get_width(), p.get_height()
            x, y = p.get_xy() 
            ax.text(x + width / 2, y + height / 2, '{:.0f}%'.format(height), ha='center', va='center', fontsize=7)

    plt.title(titulo_grafico, fontsize=9)
    plt.ylabel('Porcentaje')
    plt.xlabel('Opciones')

    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x/100:.0%}'))

    ax.yaxis.set_tick_params(labelsize=8)

    # Guardar leyenda en la variable 'handles_labels'
    handles_labels = ax.get_legend_handles_labels()

    # No mostrar la leyenda en el gráfico principal
    ax.get_legend().remove()

    st.pyplot(plt)

    # Crear una nueva figura para la leyenda
    fig_leg = plt.figure(figsize =(5, 3))
    ax_leg = fig_leg.add_subplot(111)

    # Añadir la leyenda a la nueva figura
    ax_leg.legend(*handles_labels, loc='center', title='Nomenclatura', fontsize='small')

    # No mostrar el marco del gráfico ni los ejes
    ax_leg.axis('off')

    #Gráfica de nomenclatura mostrando códigos:

    #st.pyplot(fig_leg)

    # Guardar leyenda en la variable 'handles_labels'
    handles, labels = ax.get_legend_handles_labels()

    # Limpiar las etiquetas de la leyenda para mostrar solo la etiqueta de la escala
    labels_cleaned = [label.split('-')[2] for label in labels]

    # Crear una nueva figura para la leyenda
    fig_leg = plt.figure(figsize =(5, 3))
    ax_leg = fig_leg.add_subplot(111)

    # Añadir una nueva leyenda con las etiquetas actualizadas
    ax_leg.legend(handles, labels_cleaned, loc='center', title='Nomenclatura', fontsize='small')

    # No mostrar el marco del gráfico ni los ejes
    ax_leg.axis('off')

    #st.pyplot(plt) # Este va a mostrar el gráfico sin leyenda

    st.pyplot(fig_leg) # Este va a mostrar la leyenda limpia en una figura separada


    with st.sidebar.expander("Mostrar instrucciones", expanded=False):
        st.markdown("**Instrucciones:**")
        st.write("Seleccione en las listas desplegables de la barra lateral la figura educativa y su nivel, el reactivo, el inciso del reactivo y el dato de identificación para mostrar la tabla y la gráfica de las variables seleccionadas para mostrar los resultados del Estudio de Seguimiento a los procesos de conocimiento y apropiación del plan y programas de estudio 2022. No importa el orden en el cual seleccione las cajas.")
        st.write("Una vez que haya seleccionado los campos de su elección, en la pantalla de resultados podrá ver: 1. Una tabla con los resultados de los campos seleccionados. 2. La gráfica correspondiente, y 3. La nomenclatura de los valores de la gráfica.") 
else:
    st.error("La contraseña ingresada es incorrecta.")
