from fastapi import APIRouter, HTTPException
from schemas.schemas import all_tasks
from core.db import collection
from models.models import Todo
from bson import ObjectId
from datetime import datetime

router = APIRouter()

@router.get("/")
async def get_all_todos():
    data = collection.find()
    return all_tasks(data)

# 66c25964f9f01069f6ace879

@router.get("/{task_id}")
async def find_data(task_id : str):
    try:
        id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id":id})
        if not existing_doc:
            return HTTPException(status_code=404, detail="Task does not exist.")
        resp = collection.find({"_id":id})
        return all_tasks(resp)
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")
    

@router.post("/")
async def create_task(new_task : Todo):
    try:
        resp = collection.insert_one(dict(new_task))
        return {"status_code": 200, "id":str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")
    
@router.put("/{item_id}")
async def update_task(task_id : str, updated_task : Todo):
    try:
        id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id":id, "is_deleted": False})
        if not existing_doc:
            return HTTPException(status_code=404, detail="Task does not exist.")
        update_task.updated_at = datetime.timestamp(datetime.now())
        resp = collection.update_one({"_id":id}, {"$set":dict(updated_task)})
        return {"status_code":200, "message":"Task updated successfully."}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")
    
# This uses soft delete, it only check for delete
# @router.put("/{item_id}")
# async def soft_delete_task(task_id : str, updated_task : Todo):
#     try:
#         id = ObjectId(task_id)
#         existing_doc = collection.find_one({"_id":id, "is_deleted": False})
#         if not existing_doc:
#             return HTTPException(status_code=404, detail="Task does not exist.")
#         resp = collection.update_one({"_id":id}, {"$set":{"is_deleted":True}})
#         return {"status_code":200, "message":"Task Deleted successfully."}
#     except Exception as e:
#         return HTTPException(status_code=500, detail=f"Some error occured {e}")
  
# Delete the data from the database  
@router.delete("/{item_id}")
async def delete_task(task_id : str):
    try:
        id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id":id, "is_deleted": False})
        if not existing_doc:
            return HTTPException(status_code=404, detail="Task does not exist.")
        resp = collection.delete_one({"_id":id})
        return {"status_code":200, "message":"Task Deleted successfully."}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")