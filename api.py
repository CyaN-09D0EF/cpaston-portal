from flask import Blueprint, jsonify, request, abort
from data_access import read_json, write_json

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.get("/content")
def get_content():
    return jsonify(read_json())

@api_bp.put("/content")
def put_content():
    # 전체 교체(간단명료). 필요 시 검증 로직 추가.
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        abort(400, "JSON body required")
    write_json(payload)
    return jsonify({"ok": True})

@api_bp.get("/sections/<sid>")
def get_section(sid):
    data = read_json()
    for s in data.get("sections", []):
        if s.get("id") == sid:
            return jsonify(s)
    abort(404, "section not found")

@api_bp.post("/sections")
def create_section():
    data = read_json()
    body = request.get_json(silent=True) or {}
    if not body.get("id"):
        abort(400, "id required")
    if any(s["id"] == body["id"] for s in data.get("sections", [])):
        abort(409, "id exists")
    data.setdefault("sections", []).append({
        "id": body["id"],
        "title": body.get("title", body["id"]),
        "markdown": body.get("markdown", "")
    })
    write_json(data)
    return jsonify({"ok": True}), 201

@api_bp.put("/sections/<sid>")
def update_section(sid):
    data = read_json()
    body = request.get_json(silent=True) or {}
    updated = False
    for s in data.get("sections", []):
        if s["id"] == sid:
            s.update({k:v for k,v in body.items() if k in ("title","markdown")})
            updated = True
            break
    if not updated:
        abort(404, "section not found")
    write_json(data)
    return jsonify({"ok": True})

@api_bp.delete("/sections/<sid>")
def delete_section(sid):
    data = read_json()
    before = len(data.get("sections", []))
    data["sections"] = [s for s in data.get("sections", []) if s.get("id") != sid]
    if len(data["sections"]) == before:
        abort(404, "section not found")
    write_json(data)
    return jsonify({"ok": True})
