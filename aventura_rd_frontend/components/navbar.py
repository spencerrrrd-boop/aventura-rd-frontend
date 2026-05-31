import reflex as rx

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Logo
            rx.hstack(
                rx.icon("mountain", size=28, color="#639922"),
                rx.vstack(
                    rx.text(
                        "AventuraRD",
                        font_size="20px",
                        font_weight="700",
                        color="#27500A",
                        line_height="1",
                    ),
                    rx.text(
                        "Ecoturismo & Aventura",
                        font_size="11px",
                        color="#639922",
                        line_height="1",
                    ),
                    spacing="0",
                    align="start",
                ),
                spacing="2",
                align="center",
            ),
            # Links de navegación
            rx.hstack(
                rx.link(
                    "Inicio",
                    href="/",
                    color="#27500A",
                    font_weight="500",
                    font_size="15px",
                    _hover={"color": "#639922"},
                ),
                rx.link(
                    "Aventuras",
                    href="/#ofertas",
                    color="#27500A",
                    font_weight="500",
                    font_size="15px",
                    _hover={"color": "#639922"},
                ),
                rx.link(
                    "Contacto",
                    href="/#contacto",
                    color="#27500A",
                    font_weight="500",
                    font_size="15px",
                    _hover={"color": "#639922"},
                ),
                rx.link(
                    rx.button(
                        "Reservar ahora",
                        background="#BA7517",
                        color="white",
                        border_radius="8px",
                        padding="8px 20px",
                        font_size="14px",
                        _hover={"background": "#9A6010"},
                    ),
                    href="/#ofertas",
                ),
                spacing="6",
                align="center",
                display=["none", "none", "flex"],
            ),
            justify="between",
            align="center",
            width="100%",
        ),
        background="white",
        padding="16px 40px",
        box_shadow="0 2px 8px rgba(0,0,0,0.08)",
        position="sticky",
        top="0",
        z_index="100",
        width="100%",
    )