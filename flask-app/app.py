from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html lang="es">
      <head>
        <meta charset="UTF-8" />
        <title>Demo Flask + Bootstrap</title>
        <!-- CSS de Bootstrap -->
        <link 
          rel="stylesheet" 
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
        />
      </head>
      <body class="bg-light">
        <div class="container d-flex flex-column justify-content-center align-items-center vh-100">
          <div class="card shadow p-4">
            <h1 class="display-5 text-center text-primary">Hello World desde Flask en Kubernetes!</h1>
            <p class="lead text-center mt-3">¡Se vienen cositas más geniales!</p>
            <hr>
            <div class="text-center">
              <button class="btn btn-primary">¡Haz clic aquí!</button>
            </div>
          </div>
        </div>
        <!-- JS de Bootstrap (opcional, para componentes interactivos) -->
        <script 
          src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js">
        </script>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
