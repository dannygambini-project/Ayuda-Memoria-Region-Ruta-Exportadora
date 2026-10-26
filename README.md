# Ayuda Memoria Regional 2026 - Ruta Exportadora | PROMPERÚ

Plataforma analítica e interactiva con la **Ayuda Memoria de las atenciones de la Ruta Exportadora a nivel Regional (2026)**, desarrollada para la **Subdirección de Desarrollo Exportador de PROMPERÚ**.

Consolida la información estratégica de las **25 regiones del Perú** (Amazonas, Áncash, Apurímac, Arequipa, Ayacucho, Cajamarca, Callao, Cusco, Huancavelica, Huánuco, Ica, Junín, La Libertad, Lambayeque, Lima, Loreto, Madre de Dios, Moquegua, Pasco, Piura, Puno, San Martín, Tacna, Tumbes y Ucayali).

---

## 🌐 Despliegue Manual (Paso a Paso)

El archivo central es `index.html`, una **Single Page Application (SPA)** completamente autónoma que integra la interfaz, estilos, datos de las 25 regiones y la generación de documentos Word (.docx).

### Opción 1: GitHub Pages (Recomendado)
1. Ingresa a la configuración del repositorio en GitHub:
   `https://github.com/dannygambini-project/Ayuda-Memoria-Region-Ruta-Exportadora/settings/pages`
2. En la sección **Build and deployment**:
   - **Source:** `Deploy from a branch`
   - **Branch:** `main` / carpeta `/ (root)`
3. Clic en **Save**.
4. En 1-2 minutos tu aplicación estará publicada en:
   👉 **`https://dannygambini-project.github.io/Ayuda-Memoria-Region-Ruta-Exportadora/`**

### Opción 2: Vercel
1. Ingresa a [Vercel](https://vercel.com) e inicia sesión.
2. Clic en **"Add New..."** > **"Project"**.
3. Importa el repositorio `Ayuda-Memoria-Region-Ruta-Exportadora`.
4. Deja la configuración por defecto (Framework Preset: *Other*, Root Directory: `./`).
5. Clic en **Deploy**.

### Opción 3: Netlify
1. Ingresa a [Netlify](https://app.netlify.com).
2. Selecciona **"Add new site"** > **"Import an existing project"**.
3. Conecta con GitHub y selecciona `Ayuda-Memoria-Region-Ruta-Exportadora`.
4. Publish directory: `./`
5. Clic en **Deploy site**.

### Opción 4: Ejecución Local
- Solo haz doble clic en `index.html` o ábrelo en cualquier navegador (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari).
- Funciona 100% offline sin necesidad de levantar servidores ni instalar librerías.

---

## 📈 Características Principales

1. **Dashboard Regional Interactivo:**
   - Selector rápido y dropdown alfabético con las 25 regiones del país.
   - Búsqueda en tiempo real y visualización instantánea sin recarga.

2. **Métricas Clave de Gestión (KPIs):**
   - **Empresas Atendidas 2026:** Total de empresas participantes en la Ruta Exportadora.
   - **Empresas Exportadoras:** Total y porcentaje de efectividad exportadora.
   - **Monto Exportado (FOB USD):** Cifras oficiales de exportación regional.
   - **Desglose de Categorización:** Clasificación de empresas (Inicio, Crecimiento, Consolidación).
   - **Subsectores y Mercados:** Principales partidas, sectores no tradicionales y destinos internacionales.

3. **Narrativa Ejecutiva Oficial:**
   - Redacción institucional estandarizada para autoridades y misiones técnicas.
   - Detalle desglosado de atenciones brindadas en 2026.

4. **Generador y Descargador Word (.docx):**
   - Botón *"Descargar Word"* que genera y descarga en 1 clic el documento oficial editable de la región seleccionada.

5. **Modo Impresión / Exportación a PDF:**
   - Formato preparado con reglas CSS `@media print` para generar reportes ejecutivos limpios, con membrete y tipografía optimizada.

6. **Matriz Comparativa Nacional:**
   - Modal interactivo con tabla comparativa de las 25 regiones y sus estadísticas globales.

---

## 📁 Estructura del Repositorio

| Archivo / Carpeta | Descripción |
|---|---|
| `index.html` | **Aplicación principal autónoma** (Frontend, UI, datos y lógica embebida). |
| `regiones_data.json` | Dataset consolidado en JSON con las 25 regiones, KPIs y documentos en Base64. |
| `generate_report.py` | Script Python generador de la plantilla HTML interactiva. |
| `build_data.py` | Script Python procesador de fuentes Excel y generador de `regiones_data.json`. |
| `ayuda_memoria_region_V3.ipynb` | Cuaderno Jupyter con el análisis exploratorio y pruebas de datos. |
| `documentos_word/` | Colección de los 25 documentos oficiales `.docx` individuales generados. |
| `BD EMPRESAS CATEGORIZADAS AL 2025.xlsx` | Base de datos de categorización empresarial. |
| `EXPORTACIONES 2025.xlsx` | Base de datos oficial de exportaciones regionales. |
| `base rutex 15.09.2026 - Colab.xlsx` | Registro de atenciones Ruta Exportadora (corte sept. 2026). |
| `base rutex 20.10.2026 - Colab.xlsx` | Registro de atenciones Ruta Exportadora (corte oct. 2026). |
| `.nojekyll` | Archivo para deshabilitar Jekyll en GitHub Pages. |
| `.vercelignore` | Exclusiones para optimización de despliegue en Vercel. |

---

## 🏛️ Créditos Institucionales
- **Institución:** Comisión de Promoción del Perú para la Exportación y el Turismo (**PROMPERÚ**)
- **Área:** Subdirección de Desarrollo Exportador (**DPPM**)
- **Año:** 2026
