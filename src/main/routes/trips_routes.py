from flask import jsonify, Blueprint, request

#controller
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

#repositorios
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository

#gerente de conexao 
from src.models.settings.db_connection_handler import db_connection_handler

trips_routes_bp = Blueprint("trip_routes", __name__)

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    email_repository = EmailsToInviteRepository(conn)
    controller = TripCreator(trip_repository, email_repository)
    
    response = controller.create(request.json)
    
    return jsonify(response["body"]), response["status"]

@trips_routes_bp.route("/trips/<trip_id>", methods=["GET"])
def find_trip(trip_id):
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    controller = TripFinder(trip_repository)
    
    response = controller.finder_trip_details(trip_id)
    
    return jsonify(response["body"]), response["status"]

@trips_routes_bp.route("/trips/<trip_id>/confirm", methods=["GET"])
def confirm_trip(trip_id):
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    controller = TripConfirmer(trip_repository)

    response = controller.confirm_trip(trip_id)

    return jsonify(response["body"]), response["status"]

@trips_routes_bp.route("/trips/<trip_id>/links", methods=["POST"])
def create_trip_link(trip_id):
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)
    controller = LinkCreator(link_repository)
    
    response = controller.create(request.json, trip_id)
    
    return jsonify(response["body"]), response["status"]

@trips_routes_bp.route("/trips/<trip_id>/links", methods=["GET"])
def find_trip_link(trip_id):
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)
    controller = LinkFinder(link_repository)
    
    response = controller.find(trip_id)
    
    return jsonify(response["body"]), response["status"]
