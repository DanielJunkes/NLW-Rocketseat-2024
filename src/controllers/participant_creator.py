from typing import Dict
import uuid

class ParticipantCreator():
    def __init__(self, participants_repository, email_repository) -> None:
        self.__participants_repository = participants_repository
        self.__email_repository = email_repository

    def create(self, body, trip_id: str) -> Dict:
        try:
            participant_id = str(uuid.uuid4())
            email_id = str(uuid.uuid4())
            
            email_infos = {
                "email": body["email"],
                "id": email_id,
                "trip_id": trip_id
            }
            
            participant_infos = {
                "id": participant_id,
                "trip_id": trip_id,
                "emails_to_invite_id": email_id,
                "name": body["name"]
            }

            self.__email_repository.registry_email(email_infos)
            self.__participants_repository.registry_participant(participant_infos)

            return {
                "body": {"participant_id": participant_id},
                "status": 201
            }
        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status": 400
            }