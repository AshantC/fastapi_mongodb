def individual_data(todo):
    return {
        "id" : str(todo["_id"]),
        "title" : todo["title"],
        "description" : todo["description"],
        "creation" : todo["creation"]
    }
    
def all_tasks(todos):
    return [individual_data(todo) for todo in todos]