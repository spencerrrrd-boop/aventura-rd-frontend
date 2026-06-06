import reflex as rx
import httpx
from typing import List

BACKEND_URL = "https://aventura-rd-api.onrender.com"

class DashboardStats(rx.Base):
    total_ofertas_activas: int = 0
    total_reservas: int = 0
    reservas_pendientes: int = 0
    reservas_confirmadas: int = 0
    total_ingresos: float = 0.0

class ReservaAdmin(rx.Base):
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
    token: str = ""

    @rx.event
    def set_token(self, token: str):
        self.token = token

    @rx.event
    async def cargar_dashboard(self):
        self.cargando = True
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{BACKEND_URL}/admin/dashboard",
                    headers={"Authorization": f"Bearer {self.token}"},
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
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{BACKEND_URL}/admin/reservas",
                    headers={"Authorization": f"Bearer {self.token}"},
                    timeout=10.0
                )
                if response.status_code == 200:
                    data = response.json()
                    self.reservas = [ReservaAdmin(**r) for r in data]
                    self.error = ""
                else:
                    self.error = "Error al cargar reservas"
        except Exception as e:
            self.error = f"Error de conexión: {str(e)}"
        finally:
            self.cargando = False

    @rx.event
    async def cambiar_estado_reserva(self, reserva_id: int, estado: str):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.patch(
                    f"{BACKEND_URL}/admin/reservas/{reserva_id}/estado",
                    json={"estado": estado},
                    headers={"Authorization": f"Bearer {self.token}"},
                    timeout=10.0
                )
                if response.status_code == 200:
                    return AdminState.cargar_reservas
        except Exception as e:
            self.error = f"Error: {str(e)}"