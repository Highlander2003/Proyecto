# app/routes.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

sites_bp = Blueprint('sites', __name__)

# Datos en memoria para los sitios turísticos
sites = []

@sites_bp.route('/sites', methods=['GET'])
@jwt_required()
def get_sites():
    return jsonify(sites)

@sites_bp.route('/sites', methods=['POST'])
@jwt_required()
def add_site():
    data = request.get_json()
    new_site = {
        'id': len(sites) + 1,
        'name': data['name'],
        'description': data['description']
    }
    sites.append(new_site)
    return jsonify(new_site), 201

@sites_bp.route('/sites/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_site(id):
    global sites
    sites = [site for site in sites if site['id'] != id]
    return '', 204