# aventura-rd-frontend
Frontend Reflex - AventuraRD Ecoturismo
# AventuraRD — Frontend

Plataforma web de ecoturismo y aventura AventuraRD, construida con Reflex (Python) y conectada a la API REST del backend.

## 🚀 Demo en producción

**URL:** https://aventura-rd-frontend.onrender.com

## 🛠️ Tecnologías

- Python 3.11
- Reflex 0.9.3
- httpx (cliente HTTP)
- Poetry (gestión de dependencias)
- Render (despliegue)

## 📁 Estructura de carpetas
aventura-rd-frontend/
├── aventura_rd_frontend/
│   ├── aventura_rd_frontend.py
│   ├── pages/
│   │   ├── inicio.py
│   │   ├── descripcion.py
│   │   ├── reservas.py
│   │   ├── admin_login.py
│   │   └── admin_dashboard.py
│   ├── components/
│   │   ├── navbar.py
│   │   └── footer.py
│   └── state/
│       ├── ofertas_state.py
│       ├── auth_state.py
│       └── admin_state.py
├── requirements.txt
├── rxconfig.py
└── README.md

## ⚙️ Instalación local

1. Clona el repositorio
```bash
git clone https://github.com/TU_USUARIO/aventura-rd-frontend.git
cd aventura-rd-frontend
```

2. Instala Poetry y las dependencias
```bash
poetry install
```

3. Crea el archivo `.env` basado en `.env.example`
```bash
cp .env.example .env
```

4. Configura la URL del backend en `.env`
BACKEND_URL=https://aventura-rd-api.onrender.com

5. Ejecuta el servidor
```bash
poetry run reflex run
```

## 📄 Páginas

| Página | Ruta | Descripción |
|--------|------|-------------|
| Inicio | / | Hero, ofertas, búsqueda, testimonios |
| Descripción | /descripcion/[id] | Detalle de una oferta |
| Reservas | /reservas/[id] | Formulario de reserva |
| Login Admin | /admin/login | Acceso al panel admin |
| Dashboard | /admin/dashboard | Panel de administración |

## 🔗 Repositorio Backend

https://github.com/TU_USUARIO/aventura-rd-backend

## 👥 Créditos

Desarrollado por spencer perez, elison roa. — Proyecto Final Desarrollo Web
