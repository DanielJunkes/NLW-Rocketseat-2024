from typing import Dict
import uuid

class ActivityCreator():
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository

    def create(self, body, trip_id: str) -> Dict:
        try:
            activity_id = str(uuid.uuid4())
            
            activities_infos = {
                "id": activity_id,
                "trip_id": trip_id,
                "title": body["title"],
                "occurs_at": body["occurs_at"]
            }
            
            self.__activities_repository.registry_activity(activities_infos)

            return {
                "body": {"activity_id": activity_id},
                "status": 201
            }
        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status": 400
            }