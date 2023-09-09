from flask import Flask,render_template,request,flash
import os

app = Flask(__name__)
app.secret_key  = '123'

app.config['UPLOAD_FOLDER1'] = "static/pdf"
app.config['UPLOAD_FOLDER2'] = "static/excel"
app.config['UPLOAD_FOLDER3'] = "static/video"

@app.route("/",methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        upload_pdf = request.files['upload_pdf']
        upload_excel = request.files['upload_excel']
        upload_video = request.files['upload_video']

        if upload_pdf.filename!='' and upload_excel.filename!='' and upload_video.filename!='':
            filepath1 =os.path.join(app.config["UPLOAD_FOLDER1"],upload_pdf.filename)
            filepath2 = os.path.join(app.config["UPLOAD_FOLDER2"], upload_excel.filename)
            filepath3 = os.path.join(app.config["UPLOAD_FOLDER3"], upload_video.filename)

            upload_pdf.save(filepath1)
            upload_excel.save(filepath2)
            upload_video.save(filepath3)

            flash("File upload successfully","success")

    return render_template("upload.html")
if __name__ == '__main__':
    app.run(debug=True)