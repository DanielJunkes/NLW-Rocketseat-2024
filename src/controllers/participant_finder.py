from typing import Dict

class ParticipantFinder:
    def __init__(self, participant_repository):
        self.__participant_repository = participant_repository

    def find_participants_from_trip(self, trip_id: str) -> Dict:
        try:
            participants = self.__participant_repository.find_participants_by_trip(trip_id)
        
            participants_infos = []
            
            for participant in participants:
                participants_infos.append({
                    "id": participant[0],
                    "name": participant[1],
                    "is_confirmed": participant[2],
                    "email": participant[3]
                })
                
            return {
                "body": {"participants": participants_infos}, 
                "status": 200
                }
        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status": 400
            }