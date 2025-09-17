import qrcode
import dearpygui.dearpygui as dpg

#ruta local
ruta_index = "file:///C:/Users/Alejandra/Desktop/CLUB%20DEPORTIVO%20FUTBOL%20ARTE%20AST/qr%20laboratorio/index.html"

# --- Generar QR y guardarlo ---
img = qrcode.make("file:///C:/Users/Alejandra/Desktop/CLUB%20DEPORTIVO%20FUTBOL%20ARTE%20AST/qr%20laboratorio/index.html")
img.save("qrlabo.png")

# --- Iniciar contexto DearPyGui ---
dpg.create_context()

# Registrar la textura (imagen QR)
with dpg.texture_registry():
    width, height, channels, data = dpg.load_image("qrlabo.png")
    qr_texture = dpg.add_static_texture(width, height, data)

# Ventana principal
with dpg.window(label="Visor QR", width=400, height=400):
    dpg.add_text("Código QR generado:")
    dpg.add_image(qr_texture)

dpg.child_window(width=0,height=200)
with dpg.table(header_row=True, borders_innerH=True, borders_innerV=True,borders_outerH=True, borders_outerV=True, row_background=True,tag="tabla_visitas"):


#Configuración viewport ---
dpg.create_viewport(title="Generador de QR", width=350, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()   