from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    return render_template("home.html", notes=enumerate(notes, start=1))

@app.route('/delete/<int:index>')
def delete(index):
    if 1 <= index <= len(notes):
        del notes[index - 1]
    return render_template("home.html", notes=enumerate(notes, start=1))

if __name__ == '__main__':
    app.run(debug=True)