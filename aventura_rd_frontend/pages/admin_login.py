import reflex as rx
from aventura_rd_frontend.state.auth_state import AuthState

def admin_login_page() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Logo
            rx.vstack(
                rx.hstack(
                    rx.icon("mountain", size=40, color="#639922"),
                    rx.vstack(
                        rx.text(
                            "AventuraRD",
                            font_size="28px",
                            font_weight="700",
                            color="white",
                            line_height="1",
                        ),
                        rx.text(
                            "Panel de Administración",
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
                spacing="2",
                align="center",
            ),
            # Card de login
            rx.box(
                rx.vstack(
                    rx.vstack(
                        rx.heading(
                            "Iniciar sesión",
                            size="6",
                            color="#27500A",
                            text_align="center",
                        ),
                        rx.text(
                            "Accede al panel de administración",
                            font_size="13px",
                            color="#888",
                            text_align="center",
                        ),
                        spacing="1",
                        align="center",
                    ),
                    rx.divider(border_color="#E8F5E0"),
                    # Formulario
                    rx.vstack(
                        rx.vstack(
                            rx.text(
                                "Email",
                                font_size="13px",
                                color="#555",
                                font_weight="500",
                            ),
                            rx.input(
                                placeholder="admin@aventurard.com",
                                value=AuthState.email,
                                on_change=AuthState.set_email,
                                type="email",
                                border="1.5px solid #ddd",
                                border_radius="8px",
                                padding="10px 14px",
                                width="100%",
                                _focus={"border_color": "#639922", "outline": "none"},
                            ),
                            spacing="1",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Contraseña",
                                font_size="13px",
                                color="#555",
                                font_weight="500",
                            ),
                            rx.input(
                                placeholder="••••••••",
                                value=AuthState.password,
                                on_change=AuthState.set_password,
                                type="password",
                                border="1.5px solid #ddd",
                                border_radius="8px",
                                padding="10px 14px",
                                width="100%",
                                _focus={"border_color": "#639922", "outline": "none"},
                            ),
                            spacing="1",
                            width="100%",
                        ),
                        spacing="4",
                        width="100%",
                    ),
                    # Error
                    rx.cond(
                        AuthState.error != "",
                        rx.box(
                            rx.hstack(
                                rx.icon("circle-alert", size=16, color="red"),
                                rx.text(
                                    AuthState.error,
                                    color="red",
                                    font_size="13px",
                                ),
                                spacing="2",
                                align="center",
                            ),
                            background="#FFF0F0",
                            border="1px solid #FFB3B3",
                            border_radius="8px",
                            padding="10px 14px",
                            width="100%",
                        ),
                    ),
                    # Botón
                    rx.button(
                        rx.cond(
                            AuthState.cargando,
                            rx.hstack(
                                rx.spinner(size="2"),
                                rx.text("Iniciando sesión..."),
                                spacing="2",
                            ),
                            rx.text("Iniciar sesión →"),
                        ),
                        on_click=AuthState.login,
                        background="#27500A",
                        color="white",
                        border_radius="8px",
                        padding="12px",
                        font_size="15px",
                        font_weight="600",
                        width="100%",
                        cursor="pointer",
                        _hover={"background": "#639922"},
                        disabled=AuthState.cargando,
                    ),
                    rx.hstack(
                        rx.icon("shield", size=14, color="#639922"),
                        rx.text(
                            "Acceso restringido solo para administradores",
                            font_size="12px",
                            color="#888",
                        ),
                        spacing="2",
                        align="center",
                        justify="center",
                    ),
                    spacing="5",
                    width="100%",
                ),
                background="white",
                border_radius="16px",
                padding="32px",
                box_shadow="0 8px 32px rgba(0,0,0,0.12)",
                width="100%",
                max_width="420px",
            ),
            rx.link(
                rx.hstack(
                    rx.icon("arrow-left", size=14, color="#9FCC6B"),
                    rx.text("Volver al sitio", color="#9FCC6B", font_size="13px"),
                    spacing="1",
                    align="center",
                ),
                href="/",
            ),
            spacing="8",
            align="center",
            width="100%",
            max_width="420px",
            margin="0 auto",
            padding="60px 20px",
        ),
        background="linear-gradient(135deg, #0F2006 0%, #173404 50%, #0F6E56 100%)",
        min_height="100vh",
        width="100%",
        display="flex",
        align_items="center",
        justify_content="center",
    )