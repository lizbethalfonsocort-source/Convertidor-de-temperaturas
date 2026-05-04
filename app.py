import streamlit as st

# Función para convertir las temperaturas
def convertir_temperatura(valor, de_unidad, a_unidad):
    # Si las unidades son iguales, no hay nada que convertir
    if de_unidad == a_unidad:
        return valor
    
    # Convertir primero la unidad de origen a Celsius (como punto intermedio)
    if de_unidad == "Fahrenheit":
        celsius = (valor - 32) * 5.0 / 9.0
    elif de_unidad == "Kelvin":
        celsius = valor - 273.15
    else:
        celsius = valor # Ya está en Celsius
        
    # Convertir de Celsius a la unidad de destino
    if a_unidad == "Fahrenheit":
        return (celsius * 9.0 / 5.0) + 32
    elif a_unidad == "Kelvin":
        return celsius + 273.15
    else:
        return celsius # El destino es Celsius

# Configuración de la página web
st.set_page_config(page_title="Conversor de Temperatura", page_icon="🌡️", layout="centered")

# Título y descripción
st.title("🌡️ Conversor de Temperatura")
st.write("Convierte de forma rápida y sencilla entre grados Celsius (C), Fahrenheit (F) y Kelvin (K).")

# Crear columnas para organizar los inputs de manera horizontal
col1, col2, col3 = st.columns(3)

with col1:
    # Campo para ingresar el valor numérico
    valor_input = st.number_input("Ingresa el valor:", value=0.0, format="%.2f")

with col2:
    # Menú desplegable para seleccionar la unidad original
    unidad_origen = st.selectbox("De:", ["Celsius", "Fahrenheit", "Kelvin"])

with col3:
    # Menú desplegable para seleccionar la unidad a convertir
    unidad_destino = st.selectbox("A:", ["Fahrenheit", "Celsius", "Kelvin"])

# Realizar el cálculo dinámicamente
resultado = convertir_temperatura(valor_input, unidad_origen, unidad_destino)

# Mostrar el resultado destacado
st.markdown("---")
st.subheader("Resultado de la conversión:")
st.success(f"{valor_input:.2f} {unidad_origen} equivale a **{resultado:.2f} {unidad_destino}**")