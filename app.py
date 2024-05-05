
import streamlit as st
import openai
import os

st.title("Evaluador de propuestas de grado 🐔")

openai.api_key = st.secrets["API_KEY"]

if 'openai_model' not in st.session_state:
  st.session_state['openai_model'] = 'gpt-3.5-turbo'

if 'messages' not in st.session_state:
  st.session_state['messages']=[]
  promptSystem = """Eres un profesor de Ingeniería en Computación
   que está evaluando propuestas de proyectos finales de la carrera.
  El objetivo general debe indicar qué se pretende lograr con un proyecto,
  indicando el resultado que se busca con el proyecto. Debe considerar los
  siguientes elementos: Iniciar con un verbo en infinitivo seguido del objeto de
  estudio o  problema) cómo lograrlo y opcionalmente el para qué se soluciona el
  problema. La evaluación del objetivo general debe darse sin explicaciones en términos de:
  '3: El Objetivo general es adecuado', '2: El Objetivo general es correcto
  pero debe corregirse su redacción y ortografía' o '1: El Objetivo general
  debe reformularse, no cumple con los requerimientos mínimos'.
  """

  st.session_state.messages.append({"role": "system",
                                    "content": promptSystem})

for message in st.session_state.messages:
  if message["role"] != 'system':
    with st.chat_message(message["role"]):
      st.markdown(message["content"])


if prompt := st.chat_input("Escribe algo:"):
  st.chat_message("user").markdown(prompt)
  st.session_state.messages.append({"role":"user", "content": prompt})

  response =     response = openai.Completion.create(
      engine=st.session_state['openai_model'],
      prompt=prompt,
      temperature=0.5,
      max_tokens=100
    )
  st.chat_message("assistant").markdown(response)
  st.session_state.messages.append({"role":"assistant", "content": response})
