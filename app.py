from flask import Flask, jsonify

app = Flask(__name__)
students =[{"id": 1, "name": "John", "HOD": "Jack", "Department": "EEE"},
           {"id": 2, "name": "James", "HOD": "Oliver", "Department": "ME"},
           {"id": 3, "name": "Smith", "HOD": "Meera", "Department": "ECE"},
           {"id": 4, "name": "Tina", "HOD": "Julia", "Department": "IT"},
           {"id": 5, "name": "Holia", "HOD": "Julia", "Department": "IT"}]

@app.route("/students",methods=["GET"])
def get():
    return jsonify(students)

@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    return jsonify(students[student_id])
@app.route("/students", methods=["POST"])
def create():
    student=[{"id": 5, "name": "Holia", "HOD": "Julia", "Department": "IT"}]
    students.append(student)
    return jsonify({'created':student})
@app.route("/students/<int:student_id>", methods=["PUT"])
def student_update(student_id):
    students [student_id] ['Department']="abcd"
    return jsonify({'student':students[student_id]})
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete(student_id):
    students.remove(students[student_id])
    return jsonify({'result':True})

if __name__ =='__main__':
    app.run(debug =True,port = 5000)