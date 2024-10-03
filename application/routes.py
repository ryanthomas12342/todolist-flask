from application import app
from .forms import TodoForm
from flask import render_template,flash,request,redirect,url_for
from datetime import datetime
from application import db
from bson import ObjectId

# @app.route("/")
# def index():
#     return render_template('h1.html',title='API')


@app.route("/")
def get_todos():
    print("hello")
    todos=[]
    for todo in db.todos_flask.find().sort("date_completed",-1):
        print("fnkrjfn")
        todo["_id"]=str(todo["_id"])
        todo["date_completed"]=todo["date_completed"].strftime("%b %d %Y %H:%M%S")
        todos.append(todo)
    return render_template("view_todos.html",title="view todos",todos=todos)


@app.route("/add_todo",methods=["GET","POST"])
def add_todo():

    if request.method=="POST":
        form=TodoForm(request.form)
        todo_name=form.name.data
        todo_desc=form.desc.data
        todo_select=form.completed.data
        db.todos_flask.insert_one({
            "name":todo_name,


            "description":todo_desc,
            "completed":todo_select,
            "date_completed":datetime.utcnow()
        })  
        flash("ToDO successfully added ","sucess")

        return redirect("/")
    else:
        form=TodoForm()
    return render_template("add_todo.html",form=form)





@app.route("/update/<id>",methods=["GET","POST"])
def update(id):
    if request.method=="POST":
        todo=TodoForm(request.form)

        print(todo)

        name=todo.name.data
        desc=todo.desc.data
        completed=todo.completed.data
        db.todos_flask.find_one_and_update({"_id":ObjectId(id)},{
            "$set":{
                "name":name,
                "description":desc,
                "completed":completed
            }
        })

        return  redirect("/")
    
    else:
        todo=db.todos_flask.find_one_or_404({"_id":ObjectId(id)})

        form=TodoForm()
        # print(todo)


        form.name.data=todo.get("name",None)
        form.desc.data=todo.get("description",None)
        # print(form.desc.data)
        form.completed.data=todo.get("completed",None)
        print("wow")
        

        return render_template("add_todo.html",title="UPdate",form=form)
    

@app.route("/delete/<id>")
def delete_todo(id):
    db.todos_flask.find_one_and_delete({"_id":ObjectId(id)})

    return redirect("/")







