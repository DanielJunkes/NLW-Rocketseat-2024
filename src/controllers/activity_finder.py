from typing import Dict

class ActivityFinder:
    def __init__(self, activity_repository):
        self.__activity_repository = activity_repository
        
    def find_from_trip(self, trip_id) -> Dict:
        try:
            activities = self.__activity_repository.find_activities_by_trip(trip_id)
        
            activities_formatted = []
            
            for activity in activities:
                activities_formatted.append({
                    "id": activity[0],
                    "title": activity[2],
                    "occurs_at": activity[3],
                })
                
            return {
                "body": {"activities": activities_formatted}, 
                "status": 200
                }
        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status": 400
            }