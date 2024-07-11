class LinkFinder:
    def __init__(self, link_repository) -> None:
        self.__link_repository = link_repository
        
    def find(self, trip_id):
        try:
            links = self.__link_repository.find_links_from_trip(trip_id)
            
            formatted_links = []
            for link in links:
                formatted_links.append({
                    "id": link[0],
                    "url": link[2],
                    "title": link[3],
                })
            return {
                "body": {"links": formatted_links},
                "status": 200
            }
        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status": 400
            }