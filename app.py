tasks = [
    {"title": "Read Lecture Slides", "done": True},
    {"title": "Complete Python Worksheet", "done": False},
    {"title": "Revise Git Commands", "done": True}
]

print("STUDENT TASK TRACKER:")
for task in tasks:
    status = "Done" if task["done"] else "To Do"
    print(f"- {task['title']} [{status}]")
