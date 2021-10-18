from flask import render_template,Flask,request,redirect

Text_notes={"text":[" "],"number":1}
app=Flask(__name__)

@app.route("/",methods=["GET"])
def home1():
    return render_template("index.html",n=Text_notes["number"],title=Text_notes["text"])
@app.route("/add",methods=["POST"])
def home2():
    text_Enter=request.values.get("note")
    Text_notes["text"].append(text_Enter)
    print(Text_notes["text"])
    Text_notes["number"]+=1
    print(Text_notes["number"])
    return redirect("/")

@app.route("/delet",methods=["POST"])
def home3():
    text_Enter=request.values.get("note")
    Text_notes["text"].remove(text_Enter)
    print(Text_notes["text"])
    Text_notes["number"]-=1
    print(Text_notes["number"])
    return redirect("/")
app.run(debug=True)