from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('clients/index.html')

@app.route('/ongoing-anime')
def ongoing_anime():
    return render_template('clients/ongoing_anime.html')

@app.route('/admin')
def admin():
    return render_template('admin/admin.html')

@app.route('/admin/data_anime')
def data_anime():
    return render_template('admin/data_anime.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run('0.0.0.0',port=5000,debug=True)