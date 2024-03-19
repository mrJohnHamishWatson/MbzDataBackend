from flask import Blueprint, make_response, abort, request

from db.postgres import Postgres

search_routes = Blueprint("user_routes", __name__)


class SearchController:
    @staticmethod
    @search_routes.route("/search", methods=["POST"])
    def search():
        prompt = request.get_json()['prompt']
        song = Postgres().find_song(prompt)
        if not song:
            make_response("Song doesn't exist in system", 404)
        return make_response(song.to_json(), 200)
