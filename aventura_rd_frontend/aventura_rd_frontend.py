import reflex as rx
from aventura_rd_frontend.pages.inicio import inicio_page
from aventura_rd_frontend.pages.descripcion import descripcion_page
from aventura_rd_frontend.pages.reservas import reservas_page

app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="green",
    )
)

app.add_page(inicio_page, route="/")
app.add_page(descripcion_page, route="/descripcion/[oferta_id]")
app.add_page(reservas_page, route="/reservas/[oferta_id]")