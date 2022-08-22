from flask import Flask, request, jsonify
import pymongo

#client = pymongo.MongoClient("mongodb+srv://logan:logan786@cluster0.d07rw.mongodb.net/?retryWrites=true&w=majority")

client = pymongo.MongoClient("mongodb+srv://logan:logan786@cluster0.aj5yedw.mongodb.net/?retryWrites=true&w=majority")

app= Flask(__name__)
database = client['taskdb']
collection = database['taskcollection']


@app.route("/insert/mongo", methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name: number})
        return jsonify(str("succefully inserted "))


if __name__ == '__main__':
    app.run(port=5001)
