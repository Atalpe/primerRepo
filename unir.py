import PyPDF2

def unir_pdfs(pdf_lista, salida):
    # Crear un objeto escritor de PDF
    escritor = PyPDF2.PdfWriter()
    
    # Iterar sobre la lista de archivos PDF
    for pdf in pdf_lista:
        # Abrir el archivo PDF actual
        lector = PyPDF2.PdfReader(pdf)
        # Agregar cada página del archivo PDF al escritor
        for pagina in range(len(lector.pages)):
            pagina_pdf = lector.pages[pagina]
            escritor.add_page(pagina_pdf)
    
    # Escribir el archivo PDF unido en el archivo de salida
    with open(salida, 'wb') as archivo_salida:
        escritor.write(archivo_salida)

# Lista de archivos PDF a unir
pdfs = ['1.pdf', '2.pdf']
# Archivo de salida
archivo_salida = 'Tarea 1 - Nicolas Plata.pdf'

# Llamar a la función para unir los PDFs
unir_pdfs(pdfs, archivo_salida)

print(f"Archivos PDF unidos en {archivo_salida}")


"""más cambios"""