from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        pintura = int(request.form['pintura'])
        precio = 9000
        total = pintura * precio
        descuento = 0
        if edad <= 18:
            descuento = 0
        elif edad >= 18 and edad <= 30 :
            descuento = total * 0.15
        else:
            descuento = total * 0.25

        resultado = total - descuento
        return render_template('ejercicio1.html', nombre=nombre, total=total, descuento=descuento,
                               resultado=resultado, edad=edad)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = str(request.form['usuario'])
        passw = str(request.form['passw'])
        mensaje= ''
        if usuario == 'pepe' and passw == 'user':
            mensaje = "Bienvenido usuario Pepe"
        elif usuario == 'juan' and passw == 'admin':
            mensaje = "Bienvenido administrador Juan"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template('ejercicio2.html', mensaje=mensaje, usuario=usuario, passw=passw)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run()
