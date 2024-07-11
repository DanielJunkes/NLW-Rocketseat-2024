from typing import Dict

class ParticipantConfirmer:
    def __init__(self, participants_repository) -> None:
        self.__participants_repository = participants_repository
        
    def confirm_participant(self, trip_id: str) -> Dict:
        try:
            self.__participants_repository.update_participant_status(trip_id)
        
            return {"body": None, "status": 204}
        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status": 400
            }