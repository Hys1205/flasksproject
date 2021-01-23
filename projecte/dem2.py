"""
flask的模板文件
"""
from flask import Flask,render_template,redirect,request,url_for,session
app=Flask(__name__)
app.secret_key="123456"
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
users=[
{
    "email":"123456789@qq.com",
    "password":"123456789",
}
]


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
@app.route("/login",methods=["POST","GET"])
def logins():
    if request.method=="GET":
        return render_template("login.html",**locals())
    elif request.method=="POST":
        user=None
        email=request.form.get("email")
        password=request.form.get("password")
        for u in users:
            if u["email"]==email and u["password"]==password:
                session["user"]=email
                return redirect(url_for("botter"))
    # actile=book["actile"]
    # return render_template("login.html",**locals())
@app.route("/logto")
def logtos():
    actile=book["actile"]
    return render_template("logto.html",**locals())

@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("botter"))
if __name__ == '__main__':
    app.run(debug=True)