import reflex as rx
import httpx
from pydantic import BaseModel
from typing import List

BACKEND_URL = "https://aventura-rd-api.onrender.com"

class OfertaAdmin(BaseModel):
    id: int = 0
    titulo: str = ""
    descripcion: str = ""
    imagen_url: str = ""
    precio: float = 0.0
    duracion_dias: int = 0
    destino: str = ""
    itinerario: str = ""
    cupos_disponibles: int = 0
    activa: bool = True
    categoria_id: int = 0

class OfertasAdminState(rx.State):
    ofertas: List[OfertaAdmin] = []
    cargando: bool = False
    guardando: bool = False
    error: str = ""
    mostrar_modal: bool = False
    token: str = ""

    nuevo_titulo: str = ""
    nuevo_descripcion: str = ""
    nuevo_imagen_url: str = ""
    nuevo_precio: str = ""
    nuevo_duracion: str = ""
    nuevo_destino: str = ""
    nuevo_itinerario: str = ""
    nuevo_cupos: str = ""
    nuevo_categoria_id: str = ""

    @rx.event
    def set_nuevo_titulo(self, v: str): self.nuevo_titulo = v
    @rx.event
    def set_nuevo_descripcion(self, v: str): self.nuevo_descripcion = v
    @rx.event
    def set_nuevo_imagen_url(self, v: str): self.nuevo_imagen_url = v
    @rx.event
    def set_nuevo_precio(self, v: str): self.nuevo_precio = v
    @rx.event
    def set_nuevo_duracion(self, v: str): self.nuevo_duracion = v
    @rx.event
    def set_nuevo_destino(self, v: str): self.nuevo_destino = v
    @rx.event
    def set_nuevo_itinerario(self, v: str): self.nuevo_itinerario = v
    @rx.event
    def set_nuevo_cupos(self, v: str): self.nuevo_cupos = v
    @rx.event
    def set_nuevo_categoria_id(self, v: str): self.nuevo_categoria_id = v

    @rx.event
    def set_token(self, token: str):
        self.token = token

    @rx.event
    def toggle_modal(self):
        self.mostrar_modal = not self.mostrar_modal
        self.error = ""

    @rx.event
    async def cargar_ofertas(self):
        from aventura_rd_frontend.state.admin_state import AdminState
        admin = await self.get_state(AdminState)
        self.token = admin.token
        self.cargando = True
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{BACKEND_URL}/ofertas/",
                    timeout=10.0
                )
                if response.status_code == 200:
                    data = response.json()
                    self.ofertas = [OfertaAdmin(**o) for o in data]
        except Exception as e:
            self.error = f"Error: {str(e)}"
        finally:
            self.cargando = False

    @rx.event
    async def crear_oferta(self):
        self.guardando = True
        self.error = ""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{BACKEND_URL}/admin/ofertas",
                    json={
                        "titulo": self.nuevo_titulo,
                        "descripcion": self.nuevo_descripcion,
                        "imagen_url": self.nuevo_imagen_url,
                        "precio": float(self.nuevo_precio),
                        "duracion_dias": int(self.nuevo_duracion),
                        "destino": self.nuevo_destino,
                        "itinerario": self.nuevo_itinerario,
                        "cupos_disponibles": int(self.nuevo_cupos),
                        "categoria_id": int(self.nuevo_categoria_id),
                    },
                    headers={"Authorization": f"Bearer {self.token}"},
                    timeout=10.0
                )
                if response.status_code == 201:
                    self.mostrar_modal = False
                    self.nuevo_titulo = ""
                    self.nuevo_descripcion = ""
                    self.nuevo_imagen_url = ""
                    self.nuevo_precio = ""
                    self.nuevo_duracion = ""
                    self.nuevo_destino = ""
                    self.nuevo_itinerario = ""
                    self.nuevo_cupos = ""
                    self.nuevo_categoria_id = ""
                    return OfertasAdminState.cargar_ofertas
                else:
                    data = response.json()
                    self.error = data.get("detail", "Error al crear la oferta")
        except Exception as e:
            self.error = f"Error: {str(e)}"
        finally:
            self.guardando = False

    @rx.event
    async def desactivar_oferta(self, oferta_id: int):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.delete(
                    f"{BACKEND_URL}/admin/ofertas/{oferta_id}",
                    headers={"Authorization": f"Bearer {self.token}"},
                    timeout=10.0
                )
                if response.status_code == 200:
                    return OfertasAdminState.cargar_ofertas
        except Exception as e:
            self.error = f"Error: {str(e)}"