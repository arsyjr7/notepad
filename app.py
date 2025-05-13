from flask import Flask, render_template, request, redirect, url_for
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

app = Flask(__name__)

# Konfigurasi Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note = request.form.get('note')
        if note:
            supabase.table("noteapp").insert({"text": note}).execute()

    result = supabase.table("noteapp").select("*").order("id", desc=False).execute()
    notes = result.data if result.data else []
    return render_template('index.html', notes=notes)

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    supabase.table("noteapp").delete().eq("id", note_id).execute()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
