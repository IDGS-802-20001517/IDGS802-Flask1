from flask import Flask,render_template
from flask import request
from flask import flash, redirect, url_for
import time

app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/operasbas",methods=["GET"])
def operasbas():
    return render_template("FormularioCine.html")

@app.route("/resultado1",methods=["POST"])
def resultado():
    nom=request.form.get("txtNom")
    numCom=request.form.get("txtNumCom")
    rdb=request.form.get("rdb")
    numBol=request.form.get("txtNumBol")
    des=0
    des1=0
    total=int(numCom)*int(numBol)*12
    if int(numBol)>7:
        flash("No mas de 7")
        
    if int(numBol)>5:
        des=total*.15
    if 2>int(numBol)>=5:
        des=total*.10
    if rdb=="Si":
       des1=total*.10
    cadena="Datos de compra ""\n"
    cadena=cadena+"Nombre {} ".format(nom)+"\n"
    total=total-des-des1
    cadena=cadena+"Total {} ".format(total)+"\n"
    if int(numBol)<=7:
        return render_template("resultado1.html",cadena=cadena)
    else :
        return render_template("FormularioCine.html")

if __name__ == "__main__":
    app.run(debug=True,port=3000)