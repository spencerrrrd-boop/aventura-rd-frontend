import reflex as rx
from aventura_rd_frontend.state.auth_state import AuthState
from aventura_rd_frontend.state.admin_state import AdminState

def stat_card(titulo: str, valor, color: str, icono: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon(icono, size=20, color=color),
                    background=f"rgba(255,255,255,0.1)",
                    border_radius="8px",
                    padding="8px",
                ),
                rx.spacer(),
                spacing="0",
                width="100%",
            ),
            rx.text(
                valor,
                font_size="32px",
                font_weight="700",
                color="white",
                line_height="1",
            ),
            rx.text(
                titulo,
                font_size="13px",
                color="rgba(255,255,255,0.7)",
            ),
            spacing="3",
            align="start",
            width="100%",
        ),
        background=color,
        border_radius="12px",
        padding="20px",
        width="100%",
    )

def estado_badge(estado: str) -> rx.Component:
    return rx.box(
        rx.text(estado, font_size="11px", font_weight="500"),
        background=rx.cond(
            estado == "confirmada", "#E1F5EE",
            rx.cond(
                estado == "pendiente", "#FFF8E1",
                rx.cond(
                    estado == "cancelada", "#FFEBEE",
                    "#F5FAF0"
                )
            )
        ),
        color=rx.cond(
            estado == "confirmada", "#0F6E56",
            rx.cond(
                estado == "pendiente", "#BA7517",
                rx.cond(
                    estado == "cancelada", "#C62828",
                    "#27500A"
                )
            )
        ),
        border_radius="20px",
        padding="4px 10px",
    )

def reserva_row(reserva) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text(
                    f"{reserva.nombre_cliente} {reserva.apellido_cliente}",
                    font_size="14px",
                    font_weight="500",
                    color="#27500A",
                ),
                rx.text(
                    reserva.email,
                    font_size="12px",
                    color="#888",
                ),
                spacing="0",
                align="start",
            ),
            rx.spacer(),
            rx.vstack(
                rx.text(
                    reserva.fecha_reserva,
                    font_size="12px",
                    color="#666",
                ),
                rx.text(
                    f"{reserva.num_personas} persona(s)",
                    font_size="12px",
                    color="#666",
                ),
                spacing="0",
                align="end",
            ),
            rx.vstack(
                rx.text(
                    f"RD$ {reserva.total_pago}",
                    font_size="14px",
                    font_weight="600",
                    color="#BA7517",
                ),
                estado_badge(reserva.estado),
                spacing="1",
                align="end",
            ),
            rx.vstack(
                rx.button(
                    "✓ Confirmar",
                    on_click=AdminState.cambiar_estado_reserva(reserva.id, "confirmada"),
                    background="#E1F5EE",
                    color="#0F6E56",
                    border_radius="6px",
                    padding="4px 10px",
                    font_size="11px",
                    font_weight="500",
                    cursor="pointer",
                    _hover={"background": "#0F6E56", "color": "white"},
                ),
                rx.button(
                    "✕ Cancelar",
                    on_click=AdminState.cambiar_estado_reserva(reserva.id, "cancelada"),
                    background="#FFEBEE",
                    color="#C62828",
                    border_radius="6px",
                    padding="4px 10px",
                    font_size="11px",
                    font_weight="500",
                    cursor="pointer",
                    _hover={"background": "#C62828", "color": "white"},
                ),
                spacing="1",
            ),
            spacing="4",
            align="center",
            width="100%",
        ),
        background="white",
        border_radius="10px",
        padding="16px",
        border="0.5px solid #E8F5E0",
        width="100%",
    )

def admin_dashboard_page() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Sidebar
            rx.box(
                rx.vstack(
                    # Logo
                    rx.hstack(
                        rx.icon("mountain", size=24, color="#639922"),
                        rx.text(
                            "AventuraRD",
                            font_size="16px",
                            font_weight="700",
                            color="white",
                        ),
                        spacing="2",
                        align="center",
                    ),
                    rx.text(
                        "Admin Panel",
                        font_size="11px",
                        color="#9FCC6B",
                        margin_top="-8px",
                    ),
                    rx.divider(border_color="#27500A", margin_y="16px"),
                    # Menu
                    rx.vstack(
                        rx.hstack(
                            rx.icon("layout-dashboard", size=16, color="#9FCC6B"),
                            rx.text("Dashboard", font_size="14px", color="white", font_weight="500"),
                            spacing="3",
                            align="center",
                            padding="10px 12px",
                            background="rgba(255,255,255,0.1)",
                            border_radius="8px",
                            width="100%",
                        ),
                        rx.link(
                            rx.hstack(
                                rx.icon("ticket", size=16, color="#9FCC6B"),
                                rx.text("Reservas", font_size="14px", color="#9FCC6B"),
                                spacing="3",
                                align="center",
                                padding="10px 12px",
                                width="100%",
                                _hover={"background": "rgba(255,255,255,0.05)", "border_radius": "8px"},
                            ),
                            href="#reservas",
                        ),
                        rx.link(
                            rx.hstack(
                                rx.icon("mountain", size=16, color="#9FCC6B"),
                                rx.text("Ofertas", font_size="14px", color="#9FCC6B"),
                                spacing="3",
                                align="center",
                                padding="10px 12px",
                                width="100%",
                                _hover={"background": "rgba(255,255,255,0.05)", "border_radius": "8px"},
                            ),
                            href="/",
                        ),
                        spacing="1",
                        width="100%",
                        align="start",
                    ),
                    rx.spacer(),
                    rx.divider(border_color="#27500A"),
                    # Admin info
                    rx.vstack(
                        rx.text(
                            AuthState.admin_nombre,
                            font_size="13px",
                            color="white",
                            font_weight="500",
                        ),
                        rx.text(
                            AuthState.admin_email,
                            font_size="11px",
                            color="#9FCC6B",
                        ),
                        spacing="0",
                        align="start",
                        width="100%",
                    ),
                    rx.button(
                        rx.hstack(
                            rx.icon("log-out", size=14, color="#9FCC6B"),
                            rx.text("Cerrar sesión", font_size="13px", color="#9FCC6B"),
                            spacing="2",
                            align="center",
                        ),
                        on_click=AuthState.logout,
                        background="transparent",
                        border="1px solid #27500A",
                        border_radius="8px",
                        padding="8px 12px",
                        width="100%",
                        cursor="pointer",
                        _hover={"background": "rgba(255,255,255,0.05)"},
                    ),
                    spacing="4",
                    align="start",
                    height="100vh",
                    padding="24px 16px",
                    width="220px",
                ),
                background="#0F2006",
                min_height="100vh",
                width="220px",
                position="fixed",
                left="0",
                top="0",
            ),
            # Contenido principal
            rx.box(
                rx.vstack(
                    # Header
                    rx.hstack(
                        rx.vstack(
                            rx.heading(
                                "Dashboard",
                                size="7",
                                color="#27500A",
                            ),
                            rx.text(
                                f"Bienvenido, {AuthState.admin_nombre}",
                                font_size="14px",
                                color="#888",
                            ),
                            spacing="0",
                            align="start",
                        ),
                        rx.spacer(),
                        rx.link(
                            rx.button(
                                "Ver sitio →",
                                background="#27500A",
                                color="white",
                                border_radius="8px",
                                padding="8px 16px",
                                font_size="13px",
                                _hover={"background": "#639922"},
                            ),
                            href="/",
                        ),
                        width="100%",
                        align="center",
                    ),
                    rx.divider(border_color="#E8F5E0"),
                    # Stats cards
                    rx.grid(
                        stat_card(
                            "Ofertas activas",
                            AdminState.stats.total_ofertas_activas.to_string(),
                            "#27500A",
                            "mountain",
                        ),
                        stat_card(
                            "Total reservas",
                            AdminState.stats.total_reservas.to_string(),
                            "#1D9E75",
                            "ticket",
                        ),
                        stat_card(
                            "Reservas pendientes",
                            AdminState.stats.reservas_pendientes.to_string(),
                            "#BA7517",
                            "clock",
                        ),
                        stat_card(
                            "Confirmadas",
                            AdminState.stats.reservas_confirmadas.to_string(),
                            "#639922",
                            "circle-check",
                        ),
                        columns=rx.breakpoints({"base": "2", "lg": "4"}),
                        spacing="4",
                        width="100%",
                    ),
                    # Reservas
                    rx.vstack(
                        rx.hstack(
                            rx.heading(
                                "Reservas recientes",
                                size="5",
                                color="#27500A",
                            ),
                            rx.spacer(),
                            rx.text(
                                f"Total: {AdminState.stats.total_reservas}",
                                font_size="13px",
                                color="#888",
                            ),
                            width="100%",
                            align="center",
                        ),
                        rx.cond(
                            AdminState.cargando,
                            rx.vstack(
                                rx.spinner(size="3", color="#27500A"),
                                rx.text("Cargando reservas...", color="#888"),
                                spacing="3",
                                align="center",
                                padding="40px",
                            ),
                            rx.cond(
                                AdminState.reservas.length() == 0,
                                rx.box(
                                    rx.vstack(
                                        rx.icon("inbox", size=40, color="#ddd"),
                                        rx.text(
                                            "No hay reservas aún",
                                            color="#888",
                                            font_size="14px",
                                        ),
                                        spacing="3",
                                        align="center",
                                    ),
                                    padding="40px",
                                    text_align="center",
                                    width="100%",
                                ),
                                rx.vstack(
                                    rx.foreach(
                                        AdminState.reservas,
                                        reserva_row,
                                    ),
                                    spacing="3",
                                    width="100%",
                                ),
                            ),
                        ),
                        id="reservas",
                        background="white",
                        border_radius="12px",
                        padding="24px",
                        border="0.5px solid #E8F5E0",
                        box_shadow="0 2px 8px rgba(0,0,0,0.05)",
                        width="100%",
                        spacing="4",
                    ),
                    spacing="6",
                    width="100%",
                    padding="32px",
                    align="start",
                ),
                margin_left="220px",
                min_height="100vh",
                background="#F5FAF0",
                width="calc(100% - 220px)",
            ),
            spacing="0",
            width="100%",
        ),
        width="100%",
        on_mount=[AuthState.check_auth, AdminState.cargar_dashboard, AdminState.cargar_reservas],
    )