import os
from datetime import datetime
from nicegui import ui

def procesar_texto(texto: str) -> str:
    return f"[{datetime.now().strftime('%H:%M:%S')}] Procesado OK: {texto}"

# Evita caché agresivo
ui.add_head_html('<meta http-equiv="Cache-Control" content="no-store, no-cache, must-revalidate, max-age=0" />')

@ui.page('/')
def home():
    ui.markdown("# 🌟 MetaSistema MINI")
    ui.markdown("Versión mínima para testear y desplegar en Render.")
    ui.markdown("### ✅ Procesar texto")

    ui.label("Ingresa texto")
    entrada = ui.textarea(placeholder="Escribe algo aquí...").props('autogrow')

    ui.label("Resultado")
    salida = ui.textarea().props('autogrow')

    def ejecutar():
        print("[DEBUG] Botón presionado")  # <- lo veremos en Logs de Render
        ui.notify('Procesando…', close_button='ok')
        salida.value = procesar_texto(entrada.value or "")

    with ui.row().classes('items-center gap-2'):
        ui.button("Procesar", on_click=ejecutar)
        ui.button("Ping", on_click=lambda: ui.notify("pong")).props('flat')

@ui.app.get('/health')
def health():
    return {'status': 'ok', 'time': datetime.now().isoformat()}

if __name__ in ('__main__', '__mp_main__'):
    port = int(os.getenv("PORT", 8080))
    # PROXY FIX: habilita headers de proxy para WS detrás de Render
    ui.run(
        host='0.0.0.0',
        port=port,
        title='MetaSistema MINI',
        reload=False,
        show=False,
        proxy_headers=True,           # <- clave en Render
        forwarded_allow_ips='*'       # <- acepta X-Forwarded-* de Render
    )
