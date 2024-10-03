from flask import Flask 
from flask_pymongo import PyMongo


app=Flask(__name__)

app.config['SECRET_KEY']='03954c5efe6bffc2bdc8adf20b79c7d1303586cb'
app.config['MONGO_URI']="mongodb+srv://ryanthomas2022:jgt0Ov0Utqu2aPAq@cluster0.wdjeluq.mongodb.net/todo?retryWrites=true&w=majority&appName=Cluster0"


client=PyMongo(app)

db=client.db




from application import routes