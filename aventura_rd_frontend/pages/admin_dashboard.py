import reflex as rx
from aventura_rd_frontend.state.auth_state import AuthState
from aventura_rd_frontend.state.admin_state import AdminState
from aventura_rd_frontend.state.ofertas_admin_state import OfertasAdminState

def stat_card(titulo: str, valor, color: str, icono: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon(icono, size=20, color=color),
                    background="rgba(255,255,255,0.1)",
                    border_radius="8px",
                    padding="8px",
                ),
                rx.spacer(),
                spacing="0",
                width="100%",
            ),
            rx.text(valor, font_size="32px", font_weight="700", color="white", line_height="1"),
            rx.text(titulo, font_size="13px", color="rgba(255,255,255,0.7)"),
            spacing="3", align="start", width="100%",
        ),
        background=color, border_radius="12px", padding="20px", width="100%",
    )

def estado_badge(estado: str) -> rx.Component:
    return rx.box(
        rx.text(estado, font_size="11px", font_weight="500"),
        background=rx.cond(estado == "confirmada", "#E1F5EE", rx.cond(estado == "pendiente", "#FFF8E1", rx.cond(estado == "cancelada", "#FFEBEE", "#F5FAF0"))),
        color=rx.cond(estado == "confirmada", "#0F6E56", rx.cond(estado == "pendiente", "#BA7517", rx.cond(estado == "cancelada", "#C62828", "#27500A"))),
        border_radius="20px", padding="4px 10px",
    )

def reserva_row(reserva) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text(f"{reserva.nombre_cliente} {reserva.apellido_cliente}", font_size="14px", font_weight="500", color="#27500A"),
                rx.text(reserva.email, font_size="12px", color="#888"),
                spacing="0", align="start",
            ),
            rx.spacer(),
            rx.vstack(
                rx.text(reserva.fecha_reserva, font_size="12px", color="#666"),
                rx.text(f"{reserva.num_personas} persona(s)", font_size="12px", color="#666"),
                spacing="0", align="end",
            ),
            rx.vstack(
                rx.text(f"RD$ {reserva.total_pago}", font_size="14px", font_weight="600", color="#BA7517"),
                estado_badge(reserva.estado),
                spacing="1", align="end",
            ),
            rx.vstack(
                rx.button("✓ Confirmar", on_click=AdminState.cambiar_estado_reserva(reserva.id, "confirmada"), background="#E1F5EE", color="#0F6E56", border_radius="6px", padding="4px 10px", font_size="11px", cursor="pointer", _hover={"background": "#0F6E56", "color": "white"}),
                rx.button("✕ Cancelar", on_click=AdminState.cambiar_estado_reserva(reserva.id, "cancelada"), background="#FFEBEE", color="#C62828", border_radius="6px", padding="4px 10px", font_size="11px", cursor="pointer", _hover={"background": "#C62828", "color": "white"}),
                spacing="1",
            ),
            spacing="4", align="center", width="100%",
        ),
        background="white", border_radius="10px", padding="16px", border="0.5px solid #E8F5E0", width="100%",
    )

def oferta_row_dashboard(oferta) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(src=oferta.imagen_url, width="60px", height="60px", object_fit="cover", border_radius="8px"),
            rx.vstack(
                rx.text(oferta.titulo, font_size="14px", font_weight="500", color="#27500A"),
                rx.hstack(rx.icon("map-pin", size=12, color="#639922"), rx.text(oferta.destino, font_size="12px", color="#888"), spacing="1", align="center"),
                spacing="1", align="start",
            ),
            rx.spacer(),
            rx.text(f"RD$ {oferta.precio}", font_size="14px", font_weight="600", color="#BA7517"),
            rx.text(f"{oferta.cupos_disponibles} cupos", font_size="12px", color="#666"),
            rx.box(
                rx.text(rx.cond(oferta.activa, "Activa", "Inactiva"), font_size="11px", font_weight="500"),
                background=rx.cond(oferta.activa, "#E1F5EE", "#FFEBEE"),
                color=rx.cond(oferta.activa, "#0F6E56", "#C62828"),
                border_radius="20px", padding="4px 10px",
            ),
            rx.button("✕ Desactivar", on_click=OfertasAdminState.desactivar_oferta(oferta.id), background="#FFEBEE", color="#C62828", border_radius="6px", padding="4px 10px", font_size="11px", cursor="pointer", _hover={"background": "#C62828", "color": "white"}),
            spacing="4", align="center", width="100%",
        ),
        background="white", border_radius="10px", padding="16px", border="0.5px solid #E8F5E0", width="100%",
    )

def modal_nueva_oferta() -> rx.Component:
    return rx.cond(
        OfertasAdminState.mostrar_modal,
        rx.box(
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.heading("Nueva Oferta", size="5", color="#27500A"),
                        rx.spacer(),
                        rx.button("✕", on_click=OfertasAdminState.toggle_modal, background="transparent", color="#888", cursor="pointer", font_size="18px"),
                        width="100%", align="center",
                    ),
                    rx.divider(border_color="#E8F5E0"),
                    rx.grid(
                        rx.vstack(rx.text("Título *", font_size="13px", color="#555", font_weight="500"), rx.input(placeholder="Nombre de la aventura", value=OfertasAdminState.nuevo_titulo, on_change=OfertasAdminState.set_nuevo_titulo, border="1.5px solid #ddd", border_radius="8px", padding="10px 14px", width="100%"), spacing="1", width="100%"),
                        rx.vstack(rx.text("Destino *", font_size="13px", color="#555", font_weight="500"), rx.input(placeholder="Ej: Jarabacoa, La Vega", value=OfertasAdminState.nuevo_destino, on_change=OfertasAdminState.set_nuevo_destino, border="1.5px solid #ddd", border_radius="8px", padding="10px 14px", width="100%"), spacing="1", width="100%"),
                        rx.vstack(rx.text("Precio (RD$) *", font_size="13px", color="#555", font_weight="500"), rx.input(placeholder="0.00", value=OfertasAdminState.nuevo_precio, on_change=OfertasAdminState.set_nuevo_precio, type="number", border="1.5px solid #ddd", border_radius="8px", padding="10px 14px", width="100%"), spacing="1", width="100%"),
                        rx.vstack(rx.text("Duración (días) *", font_size="13px", color="#555", font_weight="500"), rx.input(placeholder="1", value=OfertasAdminState.nuevo_duracion, on_change=OfertasAdminState.set_nuevo_duracion, type="number", border="1.5px solid #ddd", border_radius="8px", padding="10px 14px", width="100%"), spacing="1", width="100%"),
                        rx.vstack(rx.text("Cupos *", font_size="13px", color="#555", font_weight="500"), rx.input(placeholder="10", value=OfertasAdminState.nuevo_cupos, on_change=OfertasAdminState.set_nuevo_cupos, type="number", border="1.5px solid #ddd", border_radius="8px", padding="10px 14px", width="100%"), spacing="1", width="100%"),
                        rx.vstack(rx.text("Categoría ID *", font_size="13px", color="#555", font_weight="500"), rx.input(placeholder="1=Senderismo 2=Rafting 3=Zipline 4=Escalada 5=Camping 6=Ciclismo", value=OfertasAdminState.nuevo_categoria_id, on_change=OfertasAdminState.set_nuevo_categoria_id, type="number", border="1.5px solid #ddd", border_radius="8px", padding="10px 14px", width="100%"), spacing="1", width="100%"),
                        columns="2", spacing="4", width="100%",
                    ),
                    rx.vstack(rx.text("Descripción *", font_size="13px", color="#555", font_weight="500"), rx.text_area(placeholder="Descripción de la aventura...", value=OfertasAdminState.nuevo_descripcion, on_change=OfertasAdminState.set_nuevo_descripcion, border="1.5px solid #ddd", border_radius="8px", padding="10px 14px", width="100%", rows="3"), spacing="1", width="100%"),
                    rx.vstack(rx.text("Itinerario", font_size="13px", color="#555", font_weight="500"), rx.text_area(placeholder="Día 1: ...", value=OfertasAdminState.nuevo_itinerario, on_change=OfertasAdminState.set_nuevo_itinerario, border="1.5px solid #ddd", border_radius="8px", padding="10px 14px", width="100%", rows="3"), spacing="1", width="100%"),
                    rx.vstack(rx.text("URL de imagen", font_size="13px", color="#555", font_weight="500"), rx.input(placeholder="https://images.unsplash.com/...", value=OfertasAdminState.nuevo_imagen_url, on_change=OfertasAdminState.set_nuevo_imagen_url, border="1.5px solid #ddd", border_radius="8px", padding="10px 14px", width="100%"), spacing="1", width="100%"),
                    rx.cond(OfertasAdminState.error != "", rx.text(OfertasAdminState.error, color="red", font_size="13px")),
                    rx.hstack(
                        rx.button("Cancelar", on_click=OfertasAdminState.toggle_modal, background="white", color="#666", border="1px solid #ddd", border_radius="8px", padding="10px 20px", cursor="pointer"),
                        rx.button(rx.cond(OfertasAdminState.guardando, "Guardando...", "Crear oferta"), on_click=OfertasAdminState.crear_oferta, background="#27500A", color="white", border_radius="8px", padding="10px 20px", cursor="pointer", _hover={"background": "#639922"}, disabled=OfertasAdminState.guardando),
                        spacing="3", justify="end", width="100%",
                    ),
                    spacing="4", width="100%",
                ),
                background="white", border_radius="16px", padding="32px", max_width="700px", width="90%", max_height="90vh", overflow_y="auto",
            ),
            position="fixed", top="0", left="0", width="100%", height="100%",
            background="rgba(0,0,0,0.5)", display="flex", align_items="center", justify_content="center", z_index="1000",
        ),
    )

def seccion_reservas() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading("Reservas recientes", size="5", color="#27500A"),
            rx.spacer(),
            rx.text(f"Total: {AdminState.total_reservas}", font_size="13px", color="#888"),
            width="100%", align="center",
        ),
        rx.cond(
            AdminState.cargando,
            rx.vstack(rx.spinner(size="3", color="#27500A"), rx.text("Cargando reservas...", color="#888"), spacing="3", align="center", padding="40px"),
            rx.cond(
                AdminState.reservas.length() == 0,
                rx.box(rx.vstack(rx.icon("inbox", size=40, color="#ddd"), rx.text("No hay reservas aún", color="#888", font_size="14px"), spacing="3", align="center"), padding="40px", text_align="center", width="100%"),
                rx.vstack(rx.foreach(AdminState.reservas, reserva_row), spacing="3", width="100%"),
            ),
        ),
        background="white", border_radius="12px", padding="24px", border="0.5px solid #E8F5E0", box_shadow="0 2px 8px rgba(0,0,0,0.05)", width="100%", spacing="4",
    )

def seccion_ofertas() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading("Gestión de Ofertas", size="5", color="#27500A"),
            rx.spacer(),
            rx.button(
                rx.hstack(rx.icon("plus", size=16, color="white"), rx.text("Nueva oferta", color="white", font_size="14px"), spacing="2", align="center"),
                on_click=OfertasAdminState.toggle_modal, background="#27500A", border_radius="8px", padding="8px 16px", cursor="pointer", _hover={"background": "#639922"},
            ),
            width="100%", align="center",
        ),
        rx.cond(
            OfertasAdminState.cargando,
            rx.vstack(rx.spinner(size="3", color="#27500A"), rx.text("Cargando ofertas...", color="#888"), spacing="3", align="center", padding="40px"),
            rx.vstack(rx.foreach(OfertasAdminState.ofertas, oferta_row_dashboard), spacing="3", width="100%"),
        ),
        background="white", border_radius="12px", padding="24px", border="0.5px solid #E8F5E0", box_shadow="0 2px 8px rgba(0,0,0,0.05)", width="100%", spacing="4",
    )

def admin_dashboard_page() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.icon("mountain", size=24, color="#639922"),
                        rx.text("AventuraRD", font_size="16px", font_weight="700", color="white"),
                        spacing="2", align="center",
                    ),
                    rx.text("Admin Panel", font_size="11px", color="#9FCC6B", margin_top="-8px"),
                    rx.divider(border_color="#27500A", margin_y="16px"),
                    rx.vstack(
                        rx.button(
                            rx.hstack(
                                rx.icon("layout-dashboard", size=16, color="#9FCC6B"),
                                rx.text("Dashboard", font_size="14px", color=rx.cond(AdminState.seccion_activa == "reservas", "white", "#9FCC6B")),
                                spacing="3", align="center",
                            ),
                            on_click=AdminState.ver_reservas,
                            background=rx.cond(AdminState.seccion_activa == "reservas", "rgba(255,255,255,0.1)", "transparent"),
                            border="none", border_radius="8px", width="100%",
                            padding="10px 12px", cursor="pointer", justify="start",
                            _hover={"background": "rgba(255,255,255,0.05)"},
                        ),
                        rx.button(
                            rx.hstack(
                                rx.icon("mountain", size=16, color="#9FCC6B"),
                                rx.text("Ofertas", font_size="14px", color=rx.cond(AdminState.seccion_activa == "ofertas", "white", "#9FCC6B")),
                                spacing="3", align="center",
                            ),
                            on_click=AdminState.ver_ofertas,
                            background=rx.cond(AdminState.seccion_activa == "ofertas", "rgba(255,255,255,0.1)", "transparent"),
                            border="none", border_radius="8px", width="100%",
                            padding="10px 12px", cursor="pointer", justify="start",
                            _hover={"background": "rgba(255,255,255,0.05)"},
                        ),
                        spacing="1", width="100%", align="start",
                    ),
                    rx.spacer(),
                    rx.divider(border_color="#27500A"),
                    rx.vstack(
                        rx.text(AuthState.admin_nombre, font_size="13px", color="white", font_weight="500"),
                        rx.text(AuthState.admin_email, font_size="11px", color="#9FCC6B"),
                        spacing="0", align="start", width="100%",
                    ),
                    rx.button(
                        rx.hstack(rx.icon("log-out", size=14, color="#9FCC6B"), rx.text("Cerrar sesión", font_size="13px", color="#9FCC6B"), spacing="2", align="center"),
                        on_click=AuthState.logout, background="transparent", border="1px solid #27500A", border_radius="8px", padding="8px 12px", width="100%", cursor="pointer",
                    ),
                    spacing="4", align="start", height="100vh", padding="24px 16px", width="220px",
                ),
                background="#0F2006", min_height="100vh", width="220px", position="fixed", left="0", top="0",
            ),
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.vstack(
                            rx.heading("Dashboard", size="7", color="#27500A"),
                            rx.text(f"Bienvenido, {AuthState.admin_nombre}", font_size="14px", color="#888"),
                            spacing="0", align="start",
                        ),
                        rx.spacer(),
                        rx.link(rx.button("Ver sitio →", background="#27500A", color="white", border_radius="8px", padding="8px 16px", font_size="13px", _hover={"background": "#639922"}), href="/"),
                        width="100%", align="center",
                    ),
                    rx.divider(border_color="#E8F5E0"),
                    rx.grid(
                        stat_card("Ofertas activas", AdminState.total_ofertas_activas.to_string(), "#27500A", "mountain"),
                        stat_card("Total reservas", AdminState.total_reservas.to_string(), "#1D9E75", "ticket"),
                        stat_card("Reservas pendientes", AdminState.reservas_pendientes.to_string(), "#BA7517", "clock"),
                        stat_card("Confirmadas", AdminState.reservas_confirmadas.to_string(), "#639922", "circle-check"),
                        columns=rx.breakpoints({"base": "2", "lg": "4"}),
                        spacing="4", width="100%",
                    ),
                    rx.cond(
                        AdminState.seccion_activa == "reservas",
                        seccion_reservas(),
                        seccion_ofertas(),
                    ),
                    spacing="6", width="100%", padding="32px", align="start",
                ),
                margin_left="220px", min_height="100vh", background="#F5FAF0", width="calc(100% - 220px)",
            ),
            spacing="0", width="100%",
        ),
        modal_nueva_oferta(),
        width="100%",
        on_mount=[AuthState.check_auth, AdminState.cargar_dashboard, AdminState.cargar_reservas, OfertasAdminState.cargar_ofertas],
    )
