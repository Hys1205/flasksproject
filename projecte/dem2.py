"""
flask的模板文件
"""
from flask import Flask,render_template,redirect
app=Flask(__name__)
book={
    "name":"斗破大陆",
    "writer":"天蚕豆",
    "actile":[
        {
            "id":1,
            "title":"第一目录",
            "concent":"斗气化马，恐怖如斯"
        },
        {
            "id":2,
            "title": "第二目录",
            "concent": "斗气化马，恐怖如斯2"
        },
        {
            "id":3,
            "title": "第三目录",
            "concent": "斗气化马，恐怖如斯3"
        },
    ]
}

@app.route("/")
def botter():
    actile=book["actile"]
    return render_template("booter.html",**locals())
@app.route("/<int:pk>")
def footer(pk):
    actile=None
    for a in book["actile"]:
        if a["id"]==pk:
            actile=a
    return render_template("footer.html",**locals())
@app.route("/login")
def logins():
    actile=book["actile"]
    return render_template("login.html",**locals())
@app.route("/logto")
def logtos():
    actile=book["actile"]
    return render_template("logto.html",**locals())
if __name__ == '__main__':
    app.run(debug=True)