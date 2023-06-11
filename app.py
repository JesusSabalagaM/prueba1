from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    nombre = request.form.get('nombre')
    edad = request.form.get('edad')
    fecha = request.form.get('fecha')
    color = request.form.get('color')

    tipo_persona = ''
    if color == 'rojo':
        tipo_persona = 'furioso'
    elif color == 'amarillo':
        tipo_persona = 'tímido'
    elif color == 'negro':
        tipo_persona = 'alabado'

    return render_template('result.html', nombre=nombre, edad=edad, fecha=fecha, tipo_persona=tipo_persona)

if __name__ == '__main__':
    app.run(debug=True)