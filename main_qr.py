import dearpygui.dearpygui as dpg
import json

dpg.create_context()

# --- Función para guardar los datos del formulario ---
def guardar_usuario():
    try:
        with open("formulario.json", "r") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = {}

    mes = dpg.get_value("input_meses")
    if mes not in datos:
        datos[mes] = {}

    # Generar ID automático
    nuevo_id = str(len(datos[mes]) + 1)

    # Crear registro
    nuevo_usuario = {
        "Usuario": dpg.get_value("input_genero"),
        "Descripcion": dpg.get_value("input_descripcion"),
        "Instructor Responsable": dpg.get_value("input_instructor"),
        "Fecha": dpg.get_value("input_fecha"),
        "Area": dpg.get_value("input_area"),
        "SubArea": dpg.get_value("input_subarea"),
    }

    datos[mes][nuevo_id] = nuevo_usuario

    # Guardar JSON
    with open("formulario.json", "w") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    print(f"Nuevo registro agregado en {mes} con id {nuevo_id}")

# --- Tema global ---
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (255, 255, 255))
        dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0))
        dpg.add_theme_color(dpg.mvThemeCol_Button, (200, 200, 250))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (150, 200, 250))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (100, 150, 250))

# --- Ventana con formulario ---
with dpg.window(label="Formulario Registro", tag="formulario", width=500, height=400):
    dpg.add_input_text(label="Mes", tag="input_meses")
    dpg.add_input_text(label="Usuario", tag="input_genero")
    dpg.add_input_text(label="Descripción", tag="input_descripcion")
    dpg.add_input_text(label="Instructor Responsable", tag="input_instructor")
    dpg.add_input_text(label="Fecha", tag="input_fecha")
    dpg.add_input_text(label="Área", tag="input_area")
    dpg.add_input_text(label="SubÁrea", tag="input_subarea")
    dpg.add_button(label="Guardar", callback=guardar_usuario)

# Aplicar tema
dpg.bind_theme(global_theme)

# --- Mostrar interfaz ---
dpg.create_viewport(title="Formulario de Registro", width=600, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
    
