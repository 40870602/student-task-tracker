tasks = [
    {"title": "Read Lecture Slides", "done": True},
    {"title": "Complete Python Worksheet", "done": False},
    {"title": "Revise Git Commands", "done": True}
]

print("STUDENT TASK TRACKER:")
for task in tasks:
    status = "Done" if task["done"] else "To Do"
    print(f"- {task['title']} [{status}]")


completed = sum(1 for task in tasks if task["done"])
print(f"Completed tasks: {completed}/{len(tasks)}")