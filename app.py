from flask import Flask, request, send_file, render_template, jsonify
import os
import tempfile
from werkzeug.utils import secure_filename
from file_to_pdf_converter import FileToPDFConverter
import zipfile
from pathlib import Path

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

converter = FileToPDFConverter()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    try:
        # Create temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save uploaded file
            filename = secure_filename(file.filename)
            input_path = os.path.join(temp_dir, filename)
            file.save(input_path)
            
            # Convert to PDF
            output_filename = Path(filename).stem + '.pdf'
            output_path = os.path.join(temp_dir, output_filename)
            
            converter.convert_to_pdf(input_path, output_path)
            
            # Read the file content before temp directory is deleted
            with open(output_path, 'rb') as f:
                pdf_data = f.read()
            
            # Create a temporary file that won't be deleted immediately
            temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
            temp_pdf.write(pdf_data)
            temp_pdf.close()
            
            return send_file(temp_pdf.name, as_attachment=True, download_name=output_filename)
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/batch-convert', methods=['POST'])
def batch_convert():
    if 'files' not in request.files:
        return jsonify({'error': 'No files uploaded'}), 400
    
    files = request.files.getlist('files')
    if not files or all(f.filename == '' for f in files):
        return jsonify({'error': 'No files selected'}), 400
    
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            converted_files = []
            
            for file in files:
                if file.filename:
                    filename = secure_filename(file.filename)
                    input_path = os.path.join(temp_dir, filename)
                    file.save(input_path)
                    
                    output_filename = Path(filename).stem + '.pdf'
                    output_path = os.path.join(temp_dir, output_filename)
                    
                    try:
                        converter.convert_to_pdf(input_path, output_path)
                        converted_files.append((output_path, output_filename))
                    except Exception as e:
                        print(f"Error converting {filename}: {e}")
            
            if not converted_files:
                return jsonify({'error': 'No files could be converted'}), 400
            
            # Create ZIP file
            zip_path = os.path.join(temp_dir, 'converted_files.zip')
            with zipfile.ZipFile(zip_path, 'w') as zip_file:
                for file_path, filename in converted_files:
                    zip_file.write(file_path, filename)
            
            # Read ZIP content before temp directory is deleted
            with open(zip_path, 'rb') as f:
                zip_data = f.read()
            
            # Create a temporary file that won't be deleted immediately
            temp_zip = tempfile.NamedTemporaryFile(delete=False, suffix='.zip')
            temp_zip.write(zip_data)
            temp_zip.close()
            
            return send_file(temp_zip.name, as_attachment=True, download_name='converted_files.zip')
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)