
from flask import Flask, send_file
app =Flask(__name__)


@app.route('/download')
def download():
    file_path = "report.pdf"
    return send_file(file_path,as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
