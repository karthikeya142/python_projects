from flask import Flask, request, send_file, Response
from io import BytesIO

from werkzeug.utils import secure_filename

from batch_pdf_watermark import BatchPDFWatermark

app = Flask(__name__)

@app.route('/upload', methods=['GET'])
def upload_pdf():
    pdf_file = request.files.get('pdfFile')
    watermark_name = request.form.get('watermarkName')

    if not pdf_file or pdf_file.filename == '':
        return Response("Please select a PDF file to upload", status=400)

    try:
        document = BatchPDFWatermark.add_watermark(pdf_file, watermark_name)

        if document is None:
            return Response("Error occurred while processing the PDF file.", status=500)

        output_stream = BytesIO()
        document.save(output_stream)
        output_stream.seek(0)

        filename = secure_filename(pdf_file.filename)  # Ensure secure filename
        return send_file(output_stream, mimetype='application/pdf', as_attachment=True, download_name=filename)
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return Response("Error occurred while processing the PDF file.", status=500)

@app.route('/error', methods=['GET'])
def error():
    return "An error occurred."

@app.route('/download', methods=['GET'])
def download_pdf():
    pdf_data = request.args.get('pdfData')
    filename = request.args.get('filename')

    if not pdf_data or not filename:
        return Response("Invalid download request", status=400)

    return Response(pdf_data, mimetype='application/pdf', headers={
        'Content-Disposition': f'attachment;filename={filename}'
    })

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development







# from flask import Flask, request, send_file, Response
# from io import BytesIO
# from batch_pdf_watermark import BatchPDFWatermark
#
# app = Flask(__name__)
#
# @app.route('/upload', methods=['POST'])
# def upload_pdf():
#     pdf_file = request.files.get('pdfFile')
#     watermark_name = request.form.get('watermarkName')
#
#     if not pdf_file or pdf_file.filename == '':
#         return Response("Please select a PDF file to upload", status=400)
#
#     try:
#         document = BatchPDFWatermark.add_watermark(pdf_file, watermark_name)
#
#         if document is None:
#             return Response("Error occurred while processing the PDF file.", status=500)
#
#         output_stream = BytesIO()
#         document.save(output_stream)
#         output_stream.seek(0)
#
#         filename = pdf_file.filename
#         return send_file(output_stream, mimetype='application/pdf', as_attachment=True, download_name=filename)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return Response("Error occurred while processing the PDF file.", status=500)
#
# @app.route('/error', methods=['GET'])
# def error():
#     return "An error occurred."
#
# @app.route('/download', methods=['GET'])
# def download_pdf():
#     pdf_data = request.args.get('pdfData')
#     filename = request.args.get('filename')
#
#     if not pdf_data or not filename:
#         return Response("Invalid download request", status=400)
#
#     return Response(pdf_data, mimetype='application/pdf', headers={
#         'Content-Disposition': f'attachment;filename={filename}'
#     })
#
# if __name__ == '__main__':
#     app.run()
