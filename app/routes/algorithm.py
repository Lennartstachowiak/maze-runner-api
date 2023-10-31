from flask import request
from app.controller.algorithm.add_new_algorithm_controller import add_new_algorithm_controller
from app.controller.algorithm.delete_algorithm_controller import delete_algorithm_controller
from app.controller.algorithm.get_algorithms_controller import get_algorithms_controller
from app.controller.algorithm.get_single_algorithm_controller import get_single_algorithm_controller
from app.controller.algorithm.rename_algorithm_controller import rename_algorithm_controller
from app.controller.algorithm.save_algorithm_controller import save_algorithm_controller
from db import models

Mazes = models.Mazes
Algorithms = models.Algorithms


def register_algorithm_routes(api):

    @api.route("/v1/get_algorithms", methods=["GET"])
    def get_algorithms_request():
        response = get_algorithms_controller(request)
        return response

    @api.route("/v1/get_single_algorithm", methods=["GET"])
    def get_single_algorithm_request():
        response = get_single_algorithm_controller(request)
        return response

    @api.route("/v1/save_algorithm_changes", methods=["POST"])
    def save_algorithm_request():
        response = save_algorithm_controller(request)
        return response

    @api.route("/v1/add_new_algorithm", methods=["POST"])
    def add_new_algorithm_request():
        response = add_new_algorithm_controller(request)
        return response

    @api.route("/v1/delete_algorithm", methods=["DELETE"])
    def delete_algorithm_request():
        response = delete_algorithm_controller(request)
        return response

    @api.route("/v1/rename_algorithm", methods=["PATCH"])
    def rename_algorithm_request():
        response = rename_algorithm_controller(request)
        return response
