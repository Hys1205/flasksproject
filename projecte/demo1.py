from flask import Flask,render_template

app=Flask(__name__)
#路由  和页面显示
@app.route("/")
def index():
    name="小兰"
    sex="男"
    age=15
    return render_template( "index.html", **locals())
@app.route("/<int:pk>")
def detail(pk):
    return f"fghjkhsdgfjhgdsjfg{pk}"
"""
flask的模板文件
"""

if __name__ == '__main__':
    app.run(host="192.168.11.16",port="458",debug=True)

