from flask import Blueprint, request

from app.grapher import graph_ast


parse_bp = Blueprint("parse", __name__, url_prefix="/parse")

@parse_bp.route("", methods=["POST"])
def get_parse():
    body = request.get_json()

    if "code" not in body:
        return {"ok": False, "message":"Missing required attribute in body: 'code'"}, 400
    
    code = body["code"]

    try:
        graph = graph_ast(code)
    except SyntaxError as e:
        return {"ok": False, "message": str(e)}, 400

    return {"ok": True, "graph": graph}
