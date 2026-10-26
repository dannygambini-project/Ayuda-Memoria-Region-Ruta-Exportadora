# Automatización de Ayuda Memoria por Región - Ruta Exportadora

Este notebook procesa las 3 bases de datos (RUTEX, Categorías y Exportaciones 2025) para generar el resumen regional interactivo y exportar automáticamente un archivo **Word (.docx)**.

# Instalar librería python-docx para la creación del documento Word
!pip install python-docx -q

import pandas as pd
from datetime import datetime
import io
import unicodedata
from google.colab import files
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def normalizar_texto(texto):
    if pd.isna(texto):
        return ""
    texto = str(texto).strip().lower()
    # Eliminar tildes
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto

def generate_regional_document(region_to_process, df_rutex_full, df_cat_full, df_exp_full, download_file=True):
    region_norm = normalizar_texto(region_to_process)

    # Filtrar RUTEX por región
    df_rutex_reg = df_rutex_full[df_rutex_full['REGION_NORM'] == region_norm].copy()

    if df_rutex_reg.empty:
        print(f"\n[!] No se encontraron registros para la región: '{region_to_process}'. Saltando la generación del documento.")
        return

    region_nombre_oficial = df_rutex_reg['REGION'].iloc[0].strip().title()

    # --- DATOS DE ATENCIONES Y EVENTOS ---
    rucs_region = set(df_rutex_reg['RUC'].dropna().astype(str).str.strip())
    total_empresas_atendidas = len(rucs_region)

    # Actividades únicas y su ubicación
    eventos_unicos = df_rutex_reg['EVENTO'].dropna().nunique()
    df_evt_unicos = df_rutex_reg.drop_duplicates(subset=['EVENTO'])
    evt_lima = df_evt_unicos[df_evt_unicos['REGION_EVENTO'].astype(str).str.strip().str.upper() == 'LIMA'].shape[0]
    evt_regiones = eventos_unicos - evt_lima

    # --- PRINCIPALES SECTORES ---
    df_sector = df_rutex_reg.drop_duplicates(subset=['RUC', 'SECTOR'])
    sectores_counts = df_sector['SECTOR'].dropna().str.strip().value_counts()

    sectores_str_list = []
    top_sectores = sectores_counts.head(3)
    for sec_nom, sec_cant in top_sectores.items():
        pct = round((sec_cant / total_empresas_atendidas) * 100) if total_empresas_atendidas > 0 else 0
        sectores_str_list.append(f"{sec_nom} con {pct}%")

    if len(sectores_str_list) > 1:
        sectores_texto = ", ".join(sectores_str_list[:-1]) + " e " + sectores_str_list[-1]
    elif len(sectores_str_list) == 1:
        sectores_texto = sectores_str_list[0]
    else:
        sectores_texto = "sin sectores registrados"

    # --- EXPORTACIONES ---
    df_exp_filtrada = df_exp_full[df_exp_full['RUC'].astype(str).str.strip().isin(rucs_region)].copy()
    df_exp_filtrada['FOB USD'] = pd.to_numeric(df_exp_filtrada['FOB USD'], errors='coerce')
    df_exp_validas = df_exp_filtrada[df_exp_filtrada['FOB USD'] > 0]

    rucs_exportadores = set(df_exp_validas['RUC'].astype(str).str.strip())
    cant_exportadoras = len(rucs_exportadores)

    cant_mercados = df_exp_validas['MERCADO'].dropna().nunique()
    cant_productos = df_exp_validas['PARTIDA_DESCRIP_LARGA'].dropna().nunique()
    monto_fob_total_mill = df_exp_validas['FOB USD'].sum() / 1_000_000

    # Principales Productos (Partidas)
    top_productos = df_exp_validas.groupby('PARTIDA_DESCRIP_LARGA')['FOB USD'].sum().sort_values(ascending=False).head(4)
    prod_str_list = []
    for p_nom, p_monto in top_productos.items():
        m_mill = p_monto / 1_000_000
        # Eliminar el código numérico y el guion del inicio si están presentes
        if '-' in p_nom and p_nom.split('-', 1)[0].isdigit():
            display_p_nom = p_nom.split('-', 1)[1].strip()
        else:
            display_p_nom = p_nom.strip()
        prod_str_list.append(f"{display_p_nom.lower()} (USD {m_mill:,.1f} millones)")

    if prod_str_list:
        prod_texto = ", ".join(prod_str_list[:-1]) + " y " + prod_str_list[-1] if len(prod_str_list) > 1 else prod_str_list[0]
    else:
        prod_texto = "sin productos destacados"

    # Principales Mercados
    top_mercados = df_exp_validas.groupby('MERCADO')['FOB USD'].sum().sort_values(ascending=False).head(3)
    merc_str_list = []
    for m_nom, m_monto in top_mercados.items():
        m_mill = m_monto / 1_000_000
        merc_str_list.append(f"{m_nom.title()} (USD {m_mill:,.1f} millones)")

    if merc_str_list:
        merc_texto = ", ".join(merc_str_list[:-1]) + " y " + merc_str_list[-1] if len(merc_str_list) > 1 else merc_str_list[0]
    else:
        merc_texto = "sin mercados destacados"

    # --- PRINCIPALES ATENCIONES (ACTIVIDADES) ---
    top_atenciones = df_rutex_reg['EVENTO'].dropna().astype(str).str.strip().value_counts().head(15)

    # --- ARMAR TEXTO FINAL ---
    anio_actual = datetime.now().year
    mes_actual = datetime.now().strftime("%B")

    parrafo_1 = (
        f"Durante el {anio_actual} se vienen atendiendo a {total_empresas_atendidas} empresas de la región de {region_nombre_oficial}, "
        f"a través de {eventos_unicos} actividades, {evt_lima} en Lima y {evt_regiones} en regiones. "
        f"Los principales sectores son {sectores_texto}. De las {total_empresas_atendidas} empresas atendidas, "
        f"{cant_exportadoras} exportaron a {cant_mercados} mercados, {cant_productos} productos un monto de USD {monto_fob_total_mill:,.0f} millones, "
        f"siendo sus principales productos {prod_texto}. Sus principales mercados atendidos son {merc_texto}."
    )

    parrafo_atenciones_header = f"Las principales atenciones recibidas en el {anio_actual} son:"

    print("\n==================== RESUMEN GENERADO ====================\n")
    print(parrafo_1)
    print("\n" + parrafo_atenciones_header)
    for evt, cnt in top_atenciones.items():
        emp_str = "empresa" if cnt == 1 else "empresas"
        print(f"• {evt} a {cnt} {emp_str}")
    print("\n==========================================================")

    # --- CREAR DOCUMENTO WORD ---
    doc = Document()

    # Título principal
    titulo = f"Ayuda memoria de las atenciones de la Ruta Exportadora en {region_nombre_oficial} {anio_actual}"
    p_title = doc.add_paragraph()
    run_title = p_title.add_run(titulo)
    run_title.bold = True
    run_title.font.size = Pt(14)
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph() # Espacio

    # Primer párrafo informativo
    p1 = doc.add_paragraph(parrafo_1)
    p1.style.font.name = 'Arial'
    p1.style.font.size = Pt(11)

    # Encabezado de atenciones
    p_head = doc.add_paragraph(parrafo_atenciones_header)
    p_head.runs[0].bold = True
    p_head.style.font.name = 'Arial'
    p_head.style.font.size = Pt(11)

    # Lista de atenciones
    for evt, cnt in top_atenciones.items():
        emp_str = "empresa" if cnt == 1 else "empresas"
        p_item = doc.add_paragraph(f"{evt} a {cnt} {emp_str}", style='List Bullet')
        p_item.style.font.name = 'Arial'
        p_item.style.font.size = Pt(11)

    # Nombre del archivo Word
    docx_name = f"Ayuda memoria de las atenciones de la Ruta Exportadora en {region_nombre_oficial} {mes_actual} {anio_actual}.docx"
    doc.save(docx_name)

    print(f"\n[✓] ¡Documento Word generado exitosamente!: '{docx_name}'")
    if download_file:
        print("Descargando archivo Word a tu PC...")
        files.download(docx_name)
    else:
        print(f"Documento '{docx_name}' generado pero no descargado (modo 'todas').")

print("Por favor, selecciona los 3 archivos (RUTEX, Categorías y Exportaciones 2025) desde tu PC:")
uploaded = files.upload()

if len(uploaded) < 3:
    print("\n[!] Se requieren 3 archivos para procesar la información.")
else:
    dfs = {}
    for name, content in uploaded.items():
        if name.endswith('.xlsx') or name.endswith('.xls'):
            df_temp = pd.read_excel(io.BytesIO(content))
        elif name.endswith('.csv'):
            try:
                df_temp = pd.read_csv(io.BytesIO(content), encoding='utf-8')
            except:
                df_temp = pd.read_csv(io.BytesIO(content), encoding='latin1')
        else:
            continue

        df_temp.columns = df_temp.columns.str.strip()
        cols = [c.upper() for c in df_temp.columns]

        if 'EVENTO' in cols and 'REGION' in cols:
            dfs['rutex'] = df_temp
        elif 'CATEGORÍA 2025' in cols or 'CATEGORIA 2025' in cols:
            dfs['categorias'] = df_temp
        elif 'FOB USD' in cols or 'PARTIDA_DESCRIP_LARGA' in cols:
            dfs['exportaciones'] = df_temp

    df_rutex = dfs.get('rutex')
    df_cat = dfs.get('categorias')
    df_exp = dfs.get('exportaciones')

    if df_rutex is None or df_cat is None or df_exp is None:
        print("\n[!] Error: No se pudieron identificar las 3 bases. Verifica que tengan las columnas requeridas.")
    else:
        print("\nBases cargadas correctamente.")
        # Add the normalized region column to df_rutex once
        df_rutex['REGION_NORM'] = df_rutex['REGION'].apply(normalizar_texto)

        # 1. Ingresar Región a consultar
        region_input = input("\nIngresa la región que deseas consultar (ej. Tumbes, Piura, Cusco, etc.) o escribe 'todas' para generar todos los documentos: ")
        region_norm_input = normalizar_texto(region_input)

        if region_norm_input == 'todas':
            print("\nGenerando documentos para todas las regiones disponibles...")
            # Get unique official region names to iterate
            unique_regions_official = df_rutex['REGION'].dropna().unique()
            processed_regions_count = 0
            for official_region_name in unique_regions_official:
                # Only process if the normalized version of this region is actually present in the data for filtering
                if normalizar_texto(official_region_name) in df_rutex['REGION_NORM'].unique():
                    print(f"\nProcesando región: {official_region_name}")
                    generate_regional_document(official_region_name, df_rutex, df_cat, df_exp, download_file=False)
                    processed_regions_count += 1
            if processed_regions_count == 0:
                print("\n[!] No se encontraron regiones válidas para procesar.")
            else:
                print(f"\n[✓] ¡Se generaron y descargaron {processed_regions_count} documentos de las regiones!")
        else:
            generate_regional_document(region_input, df_rutex, df_cat, df_exp, download_file=True)

import zipfile
import os

# Listar todos los archivos .docx en el directorio actual
docx_files = [f for f in os.listdir('.') if f.endswith('.docx')]

if not docx_files:
    print("\n[!] No se encontraron archivos .docx para comprimir.")
else:
    zip_filename = "Ayudas_Memoria_Regiones.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for docx_file in docx_files:
            zipf.write(docx_file, os.path.basename(docx_file))
            print(f"Añadiendo {docx_file} al ZIP...")

    print(f"\n[✓] ¡Todos los documentos Word han sido comprimidos en '{zip_filename}'!")
    print("Descargando el archivo ZIP a tu PC...")
    files.download(zip_filename)


### Mover documentos generados a Google Drive

Para mover los documentos generados a Google Drive, primero necesitas montar tu Drive en Colab. Luego, el script copiará todos los archivos `.docx` del directorio actual a la carpeta especificada en tu Drive.

from google.colab import drive

# Montar Google Drive
drive.mount('/content/drive')
print("Google Drive montado exitosamente.")

import os
import shutil

# Define la ruta de la carpeta de destino en Google Drive
drive_folder_path = '/content/drive/MyDrive/DPPM 2026/PYTHON - COLAB/Proyecto colab para elaboración de AM regionales/Descargas de las ayudas memorias regionales generadas' # ¡ASEGÚRATE DE ACTUALIZAR ESTA RUTA!

# Crea la carpeta en Drive si no existe
os.makedirs(drive_folder_path, exist_ok=True)

# Obtener la lista de archivos .docx en el directorio actual para mover
docx_files_to_move = [f for f in os.listdir('.') if f.endswith('.docx')]

if not docx_files_to_move:
    print("No se encontraron nuevos archivos .docx para mover a Google Drive.")
else:
    print(f"Moviendo {len(docx_files_to_move)} archivos .docx a Google Drive...")
    for docx_file in docx_files_to_move:
        source_path = os.path.join('.', docx_file)
        destination_path = os.path.join(drive_folder_path, docx_file)
        try:
            shutil.move(source_path, destination_path)
            print(f"Movido: {docx_file} a {drive_folder_path}")
        except Exception as e:
            print(f"Error al mover {docx_file}: {e}")
    print("Todos los archivos .docx han sido movidos a Google Drive.")


