import reflex as rx
import httpx

BACKEND_URL = "http://192.168.0.100:8000"

class AuthState(rx.State):
    token: str = ""
    admin_nombre: str = ""
    admin_email: str = ""
    email: str = ""
    password: str = ""
    cargando: bool = False
    error: str = ""

    @rx.var
    def is_authenticated(self) -> bool:
        return self.token != ""

    @rx.event
    async def login(self):
        self.cargando = True
        self.error = ""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{BACKEND_URL}/auth/login",
                    json={
                        "email": self.email,
                        "password": self.password,
                    },
                    timeout=10.0
                )
                if response.status_code == 200:
                    data = response.json()
                    self.token = data["access_token"]
                    self.admin_nombre = data["admin"]["nombre"]
                    self.admin_email = data["admin"]["email"]
                    return rx.redirect("/admin/dashboard")
                else:
                    self.error = "Email o contraseña incorrectos"
        except Exception as e:
            self.error = f"Error de conexión: {str(e)}"
        finally:
            self.cargando = False

    @rx.event
    def logout(self):
        self.token = ""
        self.admin_nombre = ""
        self.admin_email = ""
        return rx.redirect("/admin/login")

    @rx.event
    def check_auth(self):
        if not self.is_authenticated:
            return rx.redirect("/admin/login")