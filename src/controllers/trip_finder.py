from typing import Dict

class TripFinder:
    def __init__(self, trip_repository) -> None:
        self.__trip_repository = trip_repository
        
    def finder_trip_details(self, trip_id) -> Dict:
        try:
            trip_details = self.__trip_repository.find_trip_by_id(trip_id)
            if not trip_details: raise Exception("Trip not found")
            
            return {
                "body": {
                    "id": trip_details[0],
                    "destination": trip_details[1],
                    "start_at": trip_details[2],
                    "end_at": trip_details[3],
                    "status": trip_details[6],
                },
                "status": 200
            }
        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status": 400
            }