# Reportes App

Aplicación web con React (frontend) y Flask (backend) para mostrar reportes.

## Estructura del Proyecto

```
reporte-react/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── venv/
│   └── data/
│       └── reportes.json
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       ├── index.css
│       └── components/
│           └── ReportTable.jsx
└── README.md
```

## Instalación y Ejecución

### Backend (Flask)

1. Navegar a la carpeta backend:
```bash
cd backend
```

2. Activar el entorno virtual:
```bash
venv\Scripts\activate
```

3. Ejecutar el servidor:
```bash
python app.py
```

El backend estará disponible en: http://localhost:5000

### Frontend (React + Vite)

1. Navegar a la carpeta frontend:
```bash
cd frontend
```

2. Ejecutar el servidor de desarrollo:
```bash
npm run dev
```

El frontend estará disponible en: http://localhost:5173

## Tecnologías Utilizadas

- **Backend**: Flask, Flask-CORS
- **Frontend**: React, Vite, Tailwind CSS
- **Datos**: JSON estático