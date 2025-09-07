from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.get("/")
def home():
    return "OK: Spotify redirect server is running."

@app.get("https://moodio-j3ay.onrender.com/callback")
def callback():
    code = request.args.get("code")
    state = request.args.get("state")
    error = request.args.get("error")

    if error:
        return f"<h1>Spotify Auth Error</h1><pre>{error}</pre>", 400
    if not code:
        return "<h1>No code in query (?code=...)</h1>", 400

    return render_template_string(f"""
    <h2>✅ Spotify auth received</h2>
    <p>Copy this code and paste it back into your Colab/Notebook (or the FULL URL):</p>
    <textarea rows="4" cols="80" readonly>{code}</textarea>
    <p><small>State: {state or "(none)"}</small></p>
    """)
