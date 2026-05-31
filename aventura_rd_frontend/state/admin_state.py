from pydantic import BaseModel as RxBase
import reflex as rx
import httpx
from typing import List
from aventura_rd_frontend.state.auth_state import AuthState

BACKEND_URL = "https://aventura-rd-api.onrender.com"

class DashboardStats(RxBase):
    total_ofertas_activas: int = 0
    total_reservas: int = 0
    reservas_pendientes: int = 0
    reservas_confirmadas: int = 0
    total_ingresos: float = 0.0

class ReservaAdmin(RxBase):
    id: int = 0
    nombre_cliente: str = ""
    apellido_cliente: str = ""
    email: str = ""
    telefono: str = ""
    oferta_id: int = 0
    fecha_reserva: str = ""
    num_personas: str = "1"
    total_pago: float = 0.0
    metodo_pago: str = ""
    estado: str = ""
    notas: str = ""
    created_at: str = ""

class AdminState(rx.State):
    stats: DashboardStats = DashboardStats()
    reservas: List[ReservaAdmin] = []
    cargando: bool = False
    error: str = ""
    reserva_seleccionada_id: int = 0
    nuevo_estado: str = "confirmada"

    @rx.event
    async def cargar_dashboard(self):
        self.cargando = True
        token = await self.get_state(AuthState)
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{BACKEND_URL}/admin/dashboard",
                    headers={"Authorization": f"Bearer {token.token}"},
                    timeout=10.0
                )
                if response.status_code == 200:
                    data = response.json()
                    self.stats = DashboardStats(**data)
                else:
                    self.error = "Error al cargar el dashboard"
        except Exception as e:
            self.error = f"Error de conexión: {str(e)}"
        finally:
            self.cargando = False

    @rx.event
    async def cargar_reservas(self):
        self.cargando = True
        token = await self.get_state(AuthState)
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{BACKEND_URL}/admin/reservas",
                    headers={"Authorization": f"Bearer {token.token}"},
                    timeout=10.0
                )
                if response.status_code == 200:
                    data = response.json()
                    self.reservas = [ReservaAdmin(**r) for r in data]
                else:
                    self.error = "Error al cargar reservas"
        except Exception as e:
            self.error = f"Error de conexión: {str(e)}"
        finally:
            self.cargando = False

    @rx.event
    async def cambiar_estado_reserva(self, reserva_id: int, estado: str):
        token = await self.get_state(AuthState)
        try:
            async with httpx.AsyncClient() as client:
                response = await client.patch(
                    f"{BACKEND_URL}/admin/reservas/{reserva_id}/estado",
                    json={"estado": estado},
                    headers={"Authorization": f"Bearer {token.token}"},
                    timeout=10.0
                )
                if response.status_code == 200:
                    return AdminState.cargar_reservas
        except Exception as e:
            self.error = f"Error: {str(e)}"