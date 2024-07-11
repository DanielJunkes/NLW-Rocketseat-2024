from typing import Dict
import uuid

class LinkCreator():
    def __init__(self, link_repository) -> None:
        self.__link_repository = link_repository
        
    def create(self, body, trip_id) -> Dict:
        try:
            link_id = str(uuid.uuid4())
            link_infos = {
                "link": body["url"],
                "trip_id": trip_id,
                "id": link_id,
                "title": body["title"]
            }
            self.__link_repository.registry_link(link_infos)
            return {
                "body": {"link_id": link_id}, 
                "status": 201
            }
        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status": 400
            }