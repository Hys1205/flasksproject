from flask import Flask

app=Flask(__name__)
@app.route("/")
def index():
    return "dasdasdsadasdasa"
@app.route("/<int:pk>")
def detail(pk):
    return f"fghjkhsdgfjhgdsjfg{pk}"
if __name__ == '__main__':
    app.run(host="192.168.11.16",port="458",debug=True)
