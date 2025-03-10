from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        user_input = request.form['user_input']
        # Eine einfache Antwortfunktion, die den Text umkehrt
        response = user_input[::-1]  # Hier kannst du auch eine komplexere Antwortlogik einbauen
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
