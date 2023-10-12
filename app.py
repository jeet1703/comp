from flask import Flask, render_template, request, send_file
import gzip
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file:
            # Read the uploaded file and compress it using gzip
            file_content = uploaded_file.read()
            compressed_file = io.BytesIO()
            with gzip.GzipFile(fileobj=compressed_file, mode='w') as f:
                f.write(file_content)

            # Return the compressed file for download
            return send_file(
                compressed_file,
                as_attachment=True,
                download_name='compressed_file.gz'
            )

    return render_template('upload.html')

@app.route('/download')
def download():
    return render_template('download.html')

if __name__ == '__main__':
    app.run(debug=True)
