from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Inisialisasi database
def init_db():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Route utama
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()

    if request.method == 'POST':
        note = request.form['note']
        c.execute("INSERT INTO notes (content) VALUES (?)", (note,))
        conn.commit()

    c.execute("SELECT * FROM notes")
    notes = c.fetchall()
    conn.close()
    return render_template('index.html', notes=notes)

# Route untuk menghapus catatan berdasarkan ID
@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
