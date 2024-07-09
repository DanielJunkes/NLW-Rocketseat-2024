import pytest
import uuid
from datetime import datetime, timedelta
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    trips_infos = {
        "id": trip_id,
        "destination": "Paris",
        "start_date": datetime.now(),
        "end_date": datetime.now() + timedelta(days=10),
        "owner_name": "John",
        "owner_email": "john@gmail.com"
    }
    
    trips_repository.create_trip(trips_infos)
    
@pytest.mark.skip(reason="Interação com o banco de dados")
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    trip = trips_repository.find_trip_by_id(trip_id)
    print(trip)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_update_status_trips():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    trips_repository.update_status_trips(trip_id)