from typing import Dict
import uuid

from src.drivers.email_sender import send_email

class TripCreator:
    def __init__(self, trip_repository, email_repository) -> None:
        self.__trip_repository = trip_repository
        self.__email_repository = email_repository
        
    def create(self, body) -> Dict:
        try:
            emails = body.get("emails_to_invite")
        
            trip_id = str(uuid.uuid4())
            trip_infos = {**body, "id": trip_id}
            
            self.__trip_repository.create_trip(trip_infos)
            
            if emails:
                for email in emails:
                    self.__email_repository.registry_email({
                        "email": email,
                        "trip_id": trip_id,
                        "id": str(uuid.uuid4())
                    })
                    
            send_email([body["owner_email"]], f"localhost:3000/trips/{trip_id}/confirm")
            
            return {
                "body": {"id": trip_id},
                "status": 201
            }
        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status": 400
            }
        