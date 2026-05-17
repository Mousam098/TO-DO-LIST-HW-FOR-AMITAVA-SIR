from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Learn Flask",
        "description": "Study Flask CRUD",
        "status": "Pending",
        "priority": "High"
    }
]

def generate_id():
    if not tasks:
        return 1
    return tasks[-1]["id"] + 1


@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):

    selected_task = None

    for task in tasks:
        if task["id"] == task_id:
            selected_task = task
            break

    if request.method == "POST":

        selected_task["title"] = request.form["title"]
        selected_task["description"] = request.form["description"]
        selected_task["status"] = request.form["status"]
        selected_task["priority"] = request.form["priority"]

        return redirect(url_for("home"))

    return render_template("edit_task.html", task=selected_task)


@app.route("/delete/<int:task_id>")
def delete_task(task_id):

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            break

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

       
