from pydantic import BaseModel as RxBase
import reflex as rx
import httpx
from typing import List

BACKEND_URL = "https://aventura-rd-api.onrender.com"

class Oferta(RxBase):
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
    categoria: dict = {}

class Categoria(RxBase):
    id: int = 0
    nombre: str = ""
    descripcion: str = ""

class OfertasState(rx.State):
    ofertas: List[Oferta] = []
    oferta_actual: Oferta = Oferta()
    categorias: List[Categoria] = []
    categoria_seleccionada: int = 0
    cargando: bool = False
    error: str = ""

    @rx.event
    async def cargar_ofertas(self):
        self.cargando = True
        self.error = ""
        try:
            async with httpx.AsyncClient() as client:
                params = {}
                if self.categoria_seleccionada > 0:
                    params["categoria_id"] = self.categoria_seleccionada
                response = await client.get(
                    f"{BACKEND_URL}/ofertas/",
                    params=params,
                    timeout=10.0
                )
                if response.status_code == 200:
                    data = response.json()
                    self.ofertas = [Oferta(**o) for o in data]
                else:
                    self.error = "Error al cargar las ofertas"
        except Exception as e:
            self.error = f"Error de conexión: {str(e)}"
        finally:
            self.cargando = False

    @rx.event
    async def cargar_categorias(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{BACKEND_URL}/categorias/",
                    timeout=10.0
                )
                if response.status_code == 200:
                    data = response.json()
                    self.categorias = [Categoria(**c) for c in data]
        except Exception as e:
            self.error = f"Error de conexión: {str(e)}"

    @rx.event
    async def cargar_oferta(self, oferta_id: int):
        self.cargando = True
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{BACKEND_URL}/ofertas/{oferta_id}",
                    timeout=10.0
                )
                if response.status_code == 200:
                    data = response.json()
                    self.oferta_actual = Oferta(**data)
                else:
                    self.error = "Oferta no encontrada"
        except Exception as e:
            self.error = f"Error de conexión: {str(e)}"
        finally:
            self.cargando = False

    @rx.event
    def filtrar_categoria(self, categoria_id: int):
        self.categoria_seleccionada = categoria_id
        return OfertasState.cargar_ofertas