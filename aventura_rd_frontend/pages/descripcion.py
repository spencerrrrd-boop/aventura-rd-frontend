import reflex as rx
from aventura_rd_frontend.components.navbar import navbar
from aventura_rd_frontend.components.footer import footer
from aventura_rd_frontend.state.ofertas_state import OfertasState

def descripcion_page() -> rx.Component:
    return rx.vstack(
        navbar(),
        # Hero de la oferta
        rx.box(
            rx.box(
                rx.vstack(
                    rx.link(
                        rx.hstack(
                            rx.icon("arrow-left", size=16, color="#9FCC6B"),
                            rx.text("Volver a aventuras", color="#9FCC6B", font_size="14px"),
                            spacing="1",
                            align="center",
                        ),
                        href="/",
                    ),
                    rx.text(
                        OfertasState.oferta_actual.categoria["nombre"],
                        color="#9FCC6B",
                        font_size="13px",
                        letter_spacing="3px",
                        font_weight="600",
                    ),
                    rx.heading(
                        OfertasState.oferta_actual.titulo,
                        size="8",
                        color="white",
                        line_height="1.1",
                    ),
                    rx.hstack(
                        rx.hstack(
                            rx.icon("map-pin", size=16, color="#9FCC6B"),
                            rx.text(
                                OfertasState.oferta_actual.destino,
                                color="white",
                                font_size="15px",
                            ),
                            spacing="1",
                            align="center",
                        ),
                        rx.hstack(
                            rx.icon("clock", size=16, color="#9FCC6B"),
                            rx.text(
                                f"{OfertasState.oferta_actual.duracion_dias} día(s)",
                                color="white",
                                font_size="15px",
                            ),
                            spacing="1",
                            align="center",
                        ),
                        rx.hstack(
                            rx.icon("users", size=16, color="#9FCC6B"),
                            rx.text(
                                f"{OfertasState.oferta_actual.cupos_disponibles} cupos disponibles",
                                color="white",
                                font_size="15px",
                            ),
                            spacing="1",
                            align="center",
                        ),
                        spacing="5",
                        flex_wrap="wrap",
                    ),
                    spacing="4",
                    align="start",
                    max_width="800px",
                ),
                background="rgba(0,0,0,0.6)",
                width="100%",
                height="100%",
                padding="80px 40px",
                display="flex",
                align_items="flex-end",
            ),
            background_image=f"url('{OfertasState.oferta_actual.imagen_url}')",
            background_size="cover",
            background_position="center",
            width="100%",
            min_height="60vh",
        ),
        # Contenido principal
        rx.box(
            rx.hstack(
                # Columna izquierda - Descripción e Itinerario
                rx.vstack(
                    # Descripción
                    rx.vstack(
                        rx.heading(
                            "Descripción general",
                            size="6",
                            color="#27500A",
                        ),
                        rx.divider(border_color="#639922", border_width="2px", width="60px"),
                        rx.text(
                            OfertasState.oferta_actual.descripcion,
                            color="#444",
                            font_size="16px",
                            line_height="1.8",
                        ),
                        spacing="3",
                        align="start",
                        width="100%",
                    ),
                    # Itinerario
                    rx.vstack(
                        rx.heading(
                            "Itinerario",
                            size="6",
                            color="#27500A",
                        ),
                        rx.divider(border_color="#639922", border_width="2px", width="60px"),
                        rx.box(
                            rx.text(
                                OfertasState.oferta_actual.itinerario,
                                color="#444",
                                font_size="15px",
                                line_height="1.8",
                            ),
                            background="#F5FAF0",
                            border_left="4px solid #639922",
                            padding="20px",
                            border_radius="0 8px 8px 0",
                            width="100%",
                        ),
                        spacing="3",
                        align="start",
                        width="100%",
                    ),
                    # Detalles
                    rx.vstack(
                        rx.heading(
                            "Detalles de la aventura",
                            size="6",
                            color="#27500A",
                        ),
                        rx.divider(border_color="#639922", border_width="2px", width="60px"),
                        rx.grid(
                            rx.box(
                                rx.hstack(
                                    rx.icon("calendar", size=20, color="#639922"),
                                    rx.vstack(
                                        rx.text("Duración", font_size="12px", color="#888"),
                                        rx.text(
                                            f"{OfertasState.oferta_actual.duracion_dias} día(s)",
                                            font_weight="600",
                                            color="#27500A",
                                        ),
                                        spacing="0",
                                    ),
                                    spacing="3",
                                    align="center",
                                ),
                                background="#F5FAF0",
                                padding="16px",
                                border_radius="8px",
                            ),
                            rx.box(
                                rx.hstack(
                                    rx.icon("map-pin", size=20, color="#639922"),
                                    rx.vstack(
                                        rx.text("Destino", font_size="12px", color="#888"),
                                        rx.text(
                                            OfertasState.oferta_actual.destino,
                                            font_weight="600",
                                            color="#27500A",
                                        ),
                                        spacing="0",
                                    ),
                                    spacing="3",
                                    align="center",
                                ),
                                background="#F5FAF0",
                                padding="16px",
                                border_radius="8px",
                            ),
                            rx.box(
                                rx.hstack(
                                    rx.icon("users", size=20, color="#639922"),
                                    rx.vstack(
                                        rx.text("Cupos", font_size="12px", color="#888"),
                                        rx.text(
                                            f"{OfertasState.oferta_actual.cupos_disponibles} disponibles",
                                            font_weight="600",
                                            color="#27500A",
                                        ),
                                        spacing="0",
                                    ),
                                    spacing="3",
                                    align="center",
                                ),
                                background="#F5FAF0",
                                padding="16px",
                                border_radius="8px",
                            ),
                            rx.box(
                                rx.hstack(
                                    rx.icon("tag", size=20, color="#639922"),
                                    rx.vstack(
                                        rx.text("Categoría", font_size="12px", color="#888"),
                                        rx.text(
                                            OfertasState.oferta_actual.categoria["nombre"],
                                            font_weight="600",
                                            color="#27500A",
                                        ),
                                        spacing="0",
                                    ),
                                    spacing="3",
                                    align="center",
                                ),
                                background="#F5FAF0",
                                padding="16px",
                                border_radius="8px",
                            ),
                            columns="2",
                            spacing="3",
                            width="100%",
                        ),
                        spacing="3",
                        align="start",
                        width="100%",
                    ),
                    spacing="8",
                    align="start",
                    width=["100%", "100%", "65%"],
                ),
                # Columna derecha - Card de reserva
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Precio por persona",
                            font_size="13px",
                            color="#888",
                        ),
                        rx.text(
                            f"RD$ {OfertasState.oferta_actual.precio:,.0f}",
                            font_size="32px",
                            font_weight="700",
                            color="#BA7517",
                        ),
                        rx.divider(border_color="#E8F5E0"),
                        rx.vstack(
                            rx.hstack(
                                rx.icon("circle-check", size=16, color="#639922"),
                                rx.text("Guía experto incluido", font_size="14px", color="#444"),
                                spacing="2", align="center",
                            ),
                            rx.hstack(
                                rx.icon("circle-check", size=16, color="#639922"),
                                rx.text("Equipamiento necesario", font_size="14px", color="#444"),
                                spacing="2", align="center",
                            ),
                            rx.hstack(
                                rx.icon("circle-check", size=16, color="#639922"),
                                rx.text("Seguro de aventura", font_size="14px", color="#444"),
                                spacing="2", align="center",
                            ),
                            rx.hstack(
                                rx.icon("circle-check", size=16, color="#639922"),
                                rx.text("Transporte incluido", font_size="14px", color="#444"),
                                spacing="2", align="center",
                            ),
                            spacing="2",
                            align="start",
                            width="100%",
                        ),
                        rx.divider(border_color="#E8F5E0"),
                        rx.link(
                            rx.button(
                                "¡Reservar esta aventura!",
                                background="#BA7517",
                                color="white",
                                border_radius="8px",
                                padding="14px",
                                font_size="16px",
                                font_weight="600",
                                width="100%",
                                cursor="pointer",
                                _hover={"background": "#9A6010"},
                            ),
                            href=f"/reservas/{OfertasState.oferta_actual.id}",
                            width="100%",
                        ),
                        rx.text(
                            "✓ Sin cargos ocultos · Cancelación flexible",
                            font_size="12px",
                            color="#888",
                            text_align="center",
                        ),
                        spacing="4",
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
                    width=["100%", "100%", "32%"],
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
        footer(),
        spacing="0",
        width="100%",
       on_mount=[OfertasState.limpiar_oferta, OfertasState.cargar_oferta_desde_url],
    )