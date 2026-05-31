import reflex as rx
from aventura_rd_frontend.components.navbar import navbar
from aventura_rd_frontend.components.footer import footer
from aventura_rd_frontend.state.ofertas_state import OfertasState

BACKEND_URL = "https://aventura-rd-api.onrender.com"

class ReservaState(rx.State):
    nombre: str = ""
    apellido: str = ""
    email: str = ""
    telefono: str = ""
    fecha_reserva: str = ""
    num_personas: str = "1"
    metodo_pago: str = "tarjeta"
    notas: str = ""
    enviando: bool = False
    exito: bool = False
    error: str = ""
    def set_nombre(self, v): self.nombre = v
    def set_apellido(self, v): self.apellido = v
    def set_email(self, v): self.email = v
    def set_telefono(self, v): self.telefono = v
    def set_fecha_reserva(self, v): self.fecha_reserva = v
    def set_num_personas(self, v): self.num_personas = v
    def set_notas(self, v): self.notas = v
    def set_metodo_pago(self, v): self.metodo_pago = v
    @rx.event
    async def enviar_reserva(self):
        import httpx
        self.enviando = True
        self.error = ""
        try:
            oferta_id = int(self.router.page.params.get("oferta_id", 1))
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{BACKEND_URL}/reservas/",
                    json={
                        "nombre_cliente": self.nombre,
                        "apellido_cliente": self.apellido,
                        "email": self.email,
                        "telefono": self.telefono,
                        "oferta_id": oferta_id,
                        "fecha_reserva": self.fecha_reserva,
                        "num_personas": self.num_personas,
                        "metodo_pago": self.metodo_pago,
                        "notas": self.notas,
                    },
                    timeout=10.0
                )
                if response.status_code == 201:
                    self.exito = True
                else:
                    data = response.json()
                    self.error = data.get("detail", "Error al procesar la reserva")
        except Exception as e:
            self.error = f"Error de conexión: {str(e)}"
        finally:
            self.enviando = False

def reservas_page() -> rx.Component:
    return rx.vstack(
        navbar(),
        # Header
        rx.box(
            rx.vstack(
                rx.link(
                    rx.hstack(
                        rx.icon("arrow-left", size=16, color="#9FCC6B"),
                        rx.text("Volver", color="#9FCC6B", font_size="14px"),
                        spacing="1",
                        align="center",
                    ),
                    href="/",
                ),
                rx.heading(
                    "Completa tu reserva",
                    size="7",
                    color="white",
                ),
                rx.text(
                    "Estás a un paso de vivir una aventura increíble",
                    color="rgba(255,255,255,0.8)",
                    font_size="16px",
                ),
                spacing="3",
                align="start",
                max_width="1200px",
                margin="0 auto",
                width="100%",
            ),
            background="linear-gradient(135deg, #0F2006 0%, #27500A 100%)",
            padding="60px 40px",
            width="100%",
        ),
        # Contenido
        rx.cond(
            ReservaState.exito,
            # Pantalla de éxito
            rx.box(
                rx.vstack(
                    rx.icon("circle-check", size=64, color="#639922"),
                    rx.heading(
                        "¡Reserva confirmada!",
                        size="7",
                        color="#27500A",
                        text_align="center",
                    ),
                    rx.text(
                        "Tu reserva fue procesada exitosamente. "
                        "Recibirás un correo de confirmación pronto.",
                        color="#666",
                        text_align="center",
                        max_width="400px",
                    ),
                    rx.link(
                        rx.button(
                            "Ver más aventuras",
                            background="#27500A",
                            color="white",
                            border_radius="8px",
                            padding="12px 28px",
                            font_size="15px",
                            _hover={"background": "#639922"},
                        ),
                        href="/",
                    ),
                    spacing="5",
                    align="center",
                    padding="80px 40px",
                ),
                width="100%",
            ),
            # Formulario
            rx.box(
                rx.hstack(
                    # Formulario izquierda
                    rx.vstack(
                        # Datos de contacto
                        rx.vstack(
                            rx.heading(
                                "1. Datos de contacto",
                                size="5",
                                color="#27500A",
                            ),
                            rx.divider(border_color="#639922", border_width="2px", width="40px"),
                            rx.grid(
                                rx.vstack(
                                    rx.text("Nombre *", font_size="13px", color="#555", font_weight="500"),
                                    rx.input(
                                        placeholder="Tu nombre",
                                        value=ReservaState.nombre,
                                        on_change=ReservaState.set_nombre,
                                        border="1.5px solid #ddd",
                                        border_radius="8px",
                                        padding="10px 14px",
                                        width="100%",
                                        _focus={"border_color": "#639922"},
                                    ),
                                    spacing="1",
                                    width="100%",
                                ),
                                rx.vstack(
                                    rx.text("Apellido *", font_size="13px", color="#555", font_weight="500"),
                                    rx.input(
                                        placeholder="Tu apellido",
                                        value=ReservaState.apellido,
                                        on_change=ReservaState.set_apellido,
                                        border="1.5px solid #ddd",
                                        border_radius="8px",
                                        padding="10px 14px",
                                        width="100%",
                                        _focus={"border_color": "#639922"},
                                    ),
                                    spacing="1",
                                    width="100%",
                                ),
                                rx.vstack(
                                    rx.text("Email *", font_size="13px", color="#555", font_weight="500"),
                                    rx.input(
                                        placeholder="tu@email.com",
                                        value=ReservaState.email,
                                        on_change=ReservaState.set_email,
                                        type="email",
                                        border="1.5px solid #ddd",
                                        border_radius="8px",
                                        padding="10px 14px",
                                        width="100%",
                                        _focus={"border_color": "#639922"},
                                    ),
                                    spacing="1",
                                    width="100%",
                                ),
                                rx.vstack(
                                    rx.text("Teléfono *", font_size="13px", color="#555", font_weight="500"),
                                    rx.input(
                                        placeholder="809-000-0000",
                                        value=ReservaState.telefono,
                                        on_change=ReservaState.set_telefono,
                                        border="1.5px solid #ddd",
                                        border_radius="8px",
                                        padding="10px 14px",
                                        width="100%",
                                        _focus={"border_color": "#639922"},
                                    ),
                                    spacing="1",
                                    width="100%",
                                ),
                                columns="2",
                                spacing="4",
                                width="100%",
                            ),
                            spacing="4",
                            align="start",
                            width="100%",
                        ),
                        # Detalles de la actividad
                        rx.vstack(
                            rx.heading(
                                "2. Detalles de la actividad",
                                size="5",
                                color="#27500A",
                            ),
                            rx.divider(border_color="#639922", border_width="2px", width="40px"),
                            rx.grid(
                                rx.vstack(
                                    rx.text("Fecha *", font_size="13px", color="#555", font_weight="500"),
                                    rx.input(
                                        type="date",
                                        value=ReservaState.fecha_reserva,
                                        on_change=ReservaState.set_fecha_reserva,
                                        border="1.5px solid #ddd",
                                        border_radius="8px",
                                        padding="10px 14px",
                                        width="100%",
                                        _focus={"border_color": "#639922"},
                                    ),
                                    spacing="1",
                                    width="100%",
                                ),
                                rx.vstack(
                                    rx.text("Número de personas *", font_size="13px", color="#555", font_weight="500"),
                                    rx.input(
                                        type="number",
                                        placeholder="1",
                                        value=ReservaState.num_personas.to_string(),
                                        on_change=ReservaState.set_num_personas,
                                        min="1",
                                        max="20",
                                        border="1.5px solid #ddd",
                                        border_radius="8px",
                                        padding="10px 14px",
                                        width="100%",
                                        _focus={"border_color": "#639922"},
                                    ),
                                    spacing="1",
                                    width="100%",
                                ),
                                columns="2",
                                spacing="4",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("Notas adicionales", font_size="13px", color="#555", font_weight="500"),
                                rx.text_area(
                                    placeholder="¿Alguna solicitud especial o pregunta?",
                                    value=ReservaState.notas,
                                    on_change=ReservaState.set_notas,
                                    border="1.5px solid #ddd",
                                    border_radius="8px",
                                    padding="10px 14px",
                                    width="100%",
                                    rows="3",
                                    _focus={"border_color": "#639922"},
                                ),
                                spacing="1",
                                width="100%",
                            ),
                            spacing="4",
                            align="start",
                            width="100%",
                        ),
                        # Método de pago
                        rx.vstack(
                            rx.heading(
                                "3. Método de pago",
                                size="5",
                                color="#27500A",
                            ),
                            rx.divider(border_color="#639922", border_width="2px", width="40px"),
                            rx.hstack(
                                rx.box(
                                    rx.vstack(
                                        rx.icon("credit-card", size=24, color="#27500A"),
                                        rx.text("Tarjeta", font_size="13px", font_weight="500", color="#27500A"),
                                        spacing="2",
                                        align="center",
                                    ),
                                    background=rx.cond(
                                        ReservaState.metodo_pago == "tarjeta",
                                        "#E8F5E0",
                                        "white"
                                    ),
                                    border=rx.cond(
                                        ReservaState.metodo_pago == "tarjeta",
                                        "2px solid #27500A",
                                        "2px solid #ddd"
                                    ),
                                    border_radius="8px",
                                    padding="16px 24px",
                                    cursor="pointer",
                                    on_click=ReservaState.set_metodo_pago("tarjeta"),
                                ),
                                rx.box(
                                    rx.vstack(
                                        rx.icon("banknote", size=24, color="#27500A"),
                                        rx.text("Efectivo", font_size="13px", font_weight="500", color="#27500A"),
                                        spacing="2",
                                        align="center",
                                    ),
                                    background=rx.cond(
                                        ReservaState.metodo_pago == "efectivo",
                                        "#E8F5E0",
                                        "white"
                                    ),
                                    border=rx.cond(
                                        ReservaState.metodo_pago == "efectivo",
                                        "2px solid #27500A",
                                        "2px solid #ddd"
                                    ),
                                    border_radius="8px",
                                    padding="16px 24px",
                                    cursor="pointer",
                                    on_click=ReservaState.set_metodo_pago("efectivo"),
                                ),
                                rx.box(
                                    rx.vstack(
                                        rx.icon("smartphone", size=24, color="#27500A"),
                                        rx.text("Transferencia", font_size="13px", font_weight="500", color="#27500A"),
                                        spacing="2",
                                        align="center",
                                    ),
                                    background=rx.cond(
                                        ReservaState.metodo_pago == "transferencia",
                                        "#E8F5E0",
                                        "white"
                                    ),
                                    border=rx.cond(
                                        ReservaState.metodo_pago == "transferencia",
                                        "2px solid #27500A",
                                        "2px solid #ddd"
                                    ),
                                    border_radius="8px",
                                    padding="16px 24px",
                                    cursor="pointer",
                                    on_click=ReservaState.set_metodo_pago("transferencia"),
                                ),
                                spacing="3",
                                flex_wrap="wrap",
                            ),
                            spacing="4",
                            align="start",
                            width="100%",
                        ),
                        # Error
                        rx.cond(
                            ReservaState.error != "",
                            rx.box(
                                rx.hstack(
                                    rx.icon("circle-alert", size=16, color="red"),
                                    rx.text(ReservaState.error, color="red", font_size="14px"),
                                    spacing="2",
                                    align="center",
                                ),
                                background="#FFF0F0",
                                border="1px solid #FFB3B3",
                                border_radius="8px",
                                padding="12px 16px",
                                width="100%",
                            ),
                        ),
                        # Botón enviar
                        rx.button(
                            rx.cond(
                                ReservaState.enviando,
                                rx.hstack(
                                    rx.spinner(size="2"),
                                    rx.text("Procesando..."),
                                    spacing="2",
                                ),
                                rx.text("Confirmar reserva →"),
                            ),
                            on_click=ReservaState.enviar_reserva,
                            background="#BA7517",
                            color="white",
                            border_radius="8px",
                            padding="14px 32px",
                            font_size="16px",
                            font_weight="600",
                            width="100%",
                            cursor="pointer",
                            _hover={"background": "#9A6010"},
                            disabled=ReservaState.enviando,
                        ),
                        spacing="8",
                        align="start",
                        width=["100%", "100%", "60%"],
                    ),
                    # Resumen derecha
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                "Resumen de tu reserva",
                                size="5",
                                color="#27500A",
                            ),
                            rx.divider(border_color="#E8F5E0"),
                            rx.image(
                                src=OfertasState.oferta_actual.imagen_url,
                                width="100%",
                                height="160px",
                                object_fit="cover",
                                border_radius="8px",
                            ),
                            rx.heading(
                                OfertasState.oferta_actual.titulo,
                                size="4",
                                color="#27500A",
                            ),
                            rx.hstack(
                                rx.icon("map-pin", size=14, color="#639922"),
                                rx.text(
                                    OfertasState.oferta_actual.destino,
                                    font_size="13px",
                                    color="#666",
                                ),
                                spacing="1",
                                align="center",
                            ),
                            rx.divider(border_color="#E8F5E0"),
                            rx.hstack(
                                rx.text("Precio por persona", font_size="14px", color="#666"),
                                rx.spacer(),
                                rx.text(
                                    f"RD$ {OfertasState.oferta_actual.precio}",
                                    font_size="14px",
                                    font_weight="600",
                                    color="#27500A",
                                ),
                                width="100%",
                            ),
                            rx.hstack(
                                rx.text("Personas", font_size="14px", color="#666"),
                                rx.spacer(),
                                rx.text(
                                    ReservaState.num_personas.to_string(),
                                    font_size="14px",
                                    font_weight="600",
                                    color="#27500A",
                                ),
                                width="100%",
                            ),
                            rx.divider(border_color="#E8F5E0"),
                            rx.hstack(
                                rx.text("Total", font_size="16px", font_weight="700", color="#27500A"),
                                rx.spacer(),
                                rx.text(
                                    f"RD$ {OfertasState.oferta_actual.precio}",
                                    font_size="20px",
                                    font_weight="700",
                                    color="#BA7517",
                                ),
                                width="100%",
                            ),
                            rx.box(
                                rx.hstack(
                                    rx.icon("shield", size=16, color="#639922"),
                                    rx.text(
                                        "Reserva 100% segura y flexible",
                                        font_size="13px",
                                        color="#639922",
                                        font_weight="500",
                                    ),
                                    spacing="2",
                                    align="center",
                                ),
                                background="#F5FAF0",
                                border_radius="8px",
                                padding="12px",
                                width="100%",
                            ),
                            spacing="3",
                            align="start",
                            width="100%",
                        ),
                        background="white",
                        border_radius="12px",
                        padding="24px",
                        box_shadow="0 4px 20px rgba(0,0,0,0.1)",
                        border="1px solid #E8F5E0",
                        position="sticky",
                        top="100px",
                        width=["100%", "100%", "37%"],
                        height="fit-content",
                    ),
                    spacing="8",
                    align="start",
                    flex_wrap=["wrap", "wrap", "nowrap"],
                    width="100%",
                ),
                max_width="1200px",
                margin="0 auto",
                padding="60px 40px",
                width="100%",
            ),
        ),
        footer(),
        spacing="0",
        width="100%",
        on_mount=OfertasState.cargar_oferta(
            rx.State.router.page.params["oferta_id"]
        ),
    )