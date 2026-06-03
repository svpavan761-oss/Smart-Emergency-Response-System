from flask import Flask, send_from_directory

app = Flask(
    __name__,
    static_folder="../frontend",
    static_url_path=""
)

# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():

    return send_from_directory(
        app.static_folder,
        "index.html"
    )

# =========================
# ALL HTML PAGES
# =========================

@app.route("/<path:path>")
def serve_files(path):

    return send_from_directory(
        app.static_folder,
        path
    )

# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )