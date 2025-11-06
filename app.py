from nicegui import ui
from datetime import datetime

def procesar_texto(texto):
    return f"[{datetime.now().strftime('%H:%M:%S')}] Procesado OK: {texto}"

# --- UI ---
ui.markdown("# 🌟 MetaSistema MINI")
ui.markdown("Versión mínima para testear y desplegar en Render.")

ui.markdown("### ✅ Procesar texto")

ui.label("Ingresa texto")
entrada = ui.textarea(placeholder="Escribe algo aquí...", auto_grow=True)

ui.label("Resultado")
salida = ui.textarea(auto_grow=True)

def ejecutar():
    salida.value = procesar_texto(entrada.value or "")

ui.button("Procesar", on_click=ejecutar)

# Ejecutar app
ui.run(title="MetaSistema MINI")
