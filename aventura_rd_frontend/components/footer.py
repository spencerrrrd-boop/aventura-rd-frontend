import reflex as rx

def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Logo y descripción
            rx.hstack(
                rx.icon("mountain", size=32, color="#639922"),
                rx.vstack(
                    rx.text(
                        "AventuraRD",
                        font_size="22px",
                        font_weight="700",
                        color="white",
                        line_height="1",
                    ),
                    rx.text(
                        "La naturaleza te llama. Nosotros te llevamos.",
                        font_size="13px",
                        color="#9FCC6B",
                        line_height="1",
                    ),
                    spacing="1",
                    align="start",
                ),
                spacing="3",
                align="center",
            ),
            # Links
            rx.hstack(
                rx.link("Inicio", href="/", color="#9FE1CB", font_size="14px", _hover={"color": "white"}),
                rx.link("Aventuras", href="/#ofertas", color="#9FE1CB", font_size="14px", _hover={"color": "white"}),
                rx.link("Reservas", href="/#ofertas", color="#9FE1CB", font_size="14px", _hover={"color": "white"}),
                rx.link("Contacto", href="/#contacto", color="#9FE1CB", font_size="14px", _hover={"color": "white"}),
                rx.link("Admin", href="/admin/login", color="#9FE1CB", font_size="14px", _hover={"color": "white"}),
                spacing="6",
                flex_wrap="wrap",
                justify="center",
            ),
            # Separador
            rx.divider(border_color="#27500A"),
            # Copyright
            rx.text(
                "© 2025 AventuraRD · Todos los derechos reservados · República Dominicana",
                color="#5DCAA5",
                font_size="12px",
                text_align="center",
            ),
            spacing="5",
            align="center",
            width="100%",
            max_width="1200px",
            margin="0 auto",
        ),
        background="#0F2006",
        padding="40px",
        width="100%",
        id="contacto",
    )