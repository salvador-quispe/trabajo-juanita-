from flask import Flask, jsonify, send_file
from flask_cors import CORS
import json
import random
import xlsxwriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

app = Flask(__name__)
CORS(app)  # Permite solicitudes desde otros orígenes (React)

# Ruta para generar el reporte en formato JSON
@app.route('/', methods=['GET'])
def get_reportes():
    # Datos simulados para el reporte
    data = {
        "total_sales": 3314,
        "total_customers": 111,
        "report_date": "2025-11-05",
        "total_revenue": 50000,  
        "average_order_value": 35.5,  
        "highest_sale": 450,  
        "lowest_sale": 25,  
        "total_orders": 95,  
        "most_purchased_product": "Producto A",  
    }

    return jsonify(data)  # Devuelve los datos en formato JSON

# Ruta para generar el archivo Excel
@app.route('/generate_excel', methods=['GET'])
def generate_excel():
    # Datos simulados para el reporte
    data = {
        "total_sales": 3314,
        "total_customers": 111,
        "report_date": "2025-11-05",
        "total_revenue": 50000,
        "average_order_value": 35.5,
        "highest_sale": 450,
        "lowest_sale": 25,
        "total_orders": 95,
        "most_purchased_product": "Producto A",
    }

    # Ruta para guardar el archivo Excel temporalmente
    excel_filename = "reporte.xlsx"
    
    # Crear un nuevo archivo Excel
    workbook = xlsxwriter.Workbook(excel_filename)
    worksheet = workbook.add_worksheet()

    # Escribir los encabezados en el archivo Excel
    worksheet.write('A1', 'Reporte de Ventas')
    worksheet.write('A2', 'Fecha del Reporte:')
    worksheet.write('B2', data['report_date'])
    worksheet.write('A3', 'Total de Ventas:')
    worksheet.write('B3', data['total_sales'])
    worksheet.write('A4', 'Total de Clientes:')
    worksheet.write('B4', data['total_customers'])
    worksheet.write('A5', 'Ingresos Totales:')
    worksheet.write('B5', data['total_revenue'])
    worksheet.write('A6', 'Valor Promedio por Orden:')
    worksheet.write('B6', data['average_order_value'])
    worksheet.write('A7', 'Venta Más Alta:')
    worksheet.write('B7', data['highest_sale'])
    worksheet.write('A8', 'Venta Más Baja:')
    worksheet.write('B8', data['lowest_sale'])
    worksheet.write('A9', 'Total de Órdenes:')
    worksheet.write('B9', data['total_orders'])
    worksheet.write('A10', 'Producto Más Comprado:')
    worksheet.write('B10', data['most_purchased_product'])

    # Cerrar el archivo Excel
    workbook.close()

    # Enviar el archivo Excel como respuesta para que el usuario lo descargue
    return send_file(excel_filename, as_attachment=True)

# Ruta para generar el PDF por sección
@app.route('/generate_pdf_sales', methods=['GET'])
def generate_pdf_sales():
    # Datos simulados para el reporte
    data = {
        "total_sales": 3314,
        "report_date": "2025-11-05",
    }

    # Ruta para guardar el archivo PDF temporalmente
    pdf_filename = "ventas_report.pdf"
    
    # Crear el PDF para ventas
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter
    c.drawString(100, height - 100, f"Reporte de Ventas - {data['report_date']}")
    c.drawString(100, height - 120, f"Total de Ventas: ${data['total_sales']}")
    c.save()

    # Enviar el archivo PDF como respuesta para que el usuario lo descargue
    return send_file(pdf_filename, as_attachment=True)

# Ruta para generar el PDF de clientes
@app.route('/generate_pdf_customers', methods=['GET'])
def generate_pdf_customers():
    # Datos simulados para el reporte
    data = {
        "total_customers": 111,
        "report_date": "2025-11-05",
    }

    # Ruta para guardar el archivo PDF temporalmente
    pdf_filename = "clientes_report.pdf"
    
    # Crear el PDF para clientes
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter
    c.drawString(100, height - 100, f"Reporte de Clientes - {data['report_date']}")
    c.drawString(100, height - 120, f"Total de Clientes: {data['total_customers']}")
    c.save()

    # Enviar el archivo PDF como respuesta para que el usuario lo descargue
    return send_file(pdf_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
