from flask import Flask
from flask import request
app=Flask(__name__)

@app.route("/operasBas",methods=["GET","POST"])
def operasBas():
    if(request.method=="POST"):
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        operacion=request.form.get("button")
        if(operacion=="suma"):
            return "<h2> La suma es :{} </h2>".format(str(int(num1)+int(num2)))
        elif(operacion=="resta"):
            return "<h2> La resta es :{} </h2>".format(str(int(num1)-int(num2)))
        elif(operacion=="division"):
            return "<h2> La division es :{} </h2>".format(str(int(num1)/int(num2)))
        elif(operacion=="multiplicacion"):
            return "<h2> La multiplicacion es :{} </h2>".format(str(int(num1)*int(num2)))
    else:
        return '''
        <form action="/operasBas" method="POST">
        <label>N1: </label>
        <input type="text" name="num1"/></br></br>
        <label>N2: </label>
        <input type="text" name="num2"/></br></br>
        <fieldset>
    <legend>Selecciona la operacion que deceas realizar:</legend>

    <div>
      <input type="radio" id="button" name="button" value="suma"
             checked>
      <label for="suma">suma</label>
    </div>

    <div>
      <input type="radio" id="button" name="button" value="resta">
      <label for="resta">resta</label>
    </div>

    <div>
      <input type="radio" id="button" name="button" value="division">
      <label for="division">division</label>
    </div>

    <div>
      <input type="radio" id="button" name="button" value="multiplicacion">
      <label for="multiplicacion">multiplicacion</label>
    </div>
</fieldset>
        <input type="submit" value="calcular"/>
        </form>
        '''

if __name__ == "__main__":
    app.run(debug=True,port=3000)