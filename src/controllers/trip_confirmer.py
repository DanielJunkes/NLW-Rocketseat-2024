from typing import Dict

class TripConfirmer:
    def __init__(self, trip_repository) -> None:
        self.__trip_repository = trip_repository
        
    def confirm_trip(self, trip_id: str) -> Dict:
        try:
            self.__trip_repository.update_status_trips(trip_id)
        
            return {"body": None, "status": 204}
        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status": 400
            }