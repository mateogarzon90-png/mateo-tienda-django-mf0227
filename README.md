# 📦 Tienda Django - Gestión de Catálogo y Descuentos

Aplicación web desarrollada con **Django** como parte del módulo formativo **MF0227_3: Programación orientada a objetos**. El proyecto permite gestionar el inventario de una tienda, aplicar lógica de negocio con Programación Orientada a Objetos (POO) para el cálculo de descuentos y ofrecer una interfaz intuitiva estilizada con Bootstrap 5.

---

## 🚀 Características

- **Gestión de productos:** Registro y listado de productos con atributos como nombre, precio y porcentaje de descuento.
- **Lógica de negocio con POO:** Implementación de clases en Python (`ProductoBase` y `ProductoOferta`) para el cálculo dinámico de precios finales.
- **Validaciones en modelos y formularios:** Garantía de precios no negativos y descuentos dentro del rango de 0% a 100%.
- **Interfaz moderna:** Plantillas HTML5 responsivas utilizando Bootstrap 5 via CDN.
- **Pruebas automatizadas:** Cobertura de tests para verificar la lógica de descuentos y las respuestas HTTP del servidor.

---

## 🛠️ Requisitos e Instalación

### Prerrequisitos
- Python 3.8 o superior

### Pasos para la ejecución local

1. **Clonar o descargar el repositorio:**
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd tienda
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En macOS/Linux
   # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install django
   ```

4. **Aplicar las migraciones de la base de datos:**
   ```bash
   python3 manage.py migrate
   ```

5. **Ejecutar el servidor de desarrollo:**
   ```bash
   python3 manage.py runserver
   ```

6. **Acceder a la aplicación:**
   Abre tu navegador e ingresa a `http://127.0.0.1:8000/productos/`

---

## 🧪 Ejecución de Pruebas Automatizadas

El proyecto cuenta con suites de pruebas unitarias creadas en `catalogo/tests.py`. Para ejecutarlas:

```bash
python3 manage.py test catalogo
```

---

## 🔒 Medidas de Seguridad para Producción

Antes de realizar el despliegue en un entorno de producción real, es fundamental aplicar la siguiente medida de seguridad:

* **Desactivación del Modo Depuración (`DEBUG = False`):**
  En el archivo `tienda/settings.py`, se debe cambiar la configuración a `DEBUG = False`. Al mantener `DEBUG = True` en producción, cualquier error imprevisto expondrá trazas completas del código fuente, variables de entorno, claves secretas e información sensible de la base de datos a los usuarios finales. Además, se debe configurar la lista de dominios permitidos en `ALLOWED_HOSTS`.

  Mateo Garzon