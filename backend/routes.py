# =====================================
# SPAM X - routes.py
# Smart Emergency Response System
# =====================================

from flask import Blueprint, request, jsonify

from database import (
    get_all_users,
    add_user,
    validate_login,
    get_available_hospitals,
    find_donors_by_blood_group
)

from emergency import (
    send_sos_alert,
    request_ambulance
)

# -------------------------------------
# CREATE BLUEPRINT
# -------------------------------------

routes = Blueprint("routes", __name__)


# =====================================
# HOME ROUTE
# =====================================

@routes.route("/")
def home():

    return jsonify({
        "message": "🚨 Welcome to SPAM X Emergency System"
    })


# =====================================
# REGISTER ROUTE
# =====================================

@routes.route("/register", methods=["POST"])
def register():

    data = request.json

    new_user = {

        "id": len(get_all_users()) + 1,
        "name": data.get("name"),
        "email": data.get("email"),
        "password": data.get("password"),
        "phone": data.get("phone"),
        "location": data.get("location")

    }

    add_user(new_user)

    return jsonify({
        "success": True,
        "message": "✅ User Registered Successfully"
    })


# =====================================
# LOGIN ROUTE
# =====================================

@routes.route("/login", methods=["POST"])
def login():

    data = request.json

    email = data.get("email")
    password = data.get("password")

    valid = validate_login(email, password)

    if valid:

        return jsonify({
            "success": True,
            "message": "✅ Login Successful"
        })

    else:

        return jsonify({
            "success": False,
            "message": "❌ Invalid Email or Password"
        })


# =====================================
# HOSPITAL ROUTE
# =====================================

@routes.route("/hospitals", methods=["GET"])
def hospitals():

    hospital_data = get_available_hospitals()

    return jsonify({
        "success": True,
        "hospitals": hospital_data
    })


# =====================================
# BLOOD DONOR ROUTE
# =====================================

@routes.route("/donors/<blood_group>", methods=["GET"])
def donors(blood_group):

    donor_data = find_donors_by_blood_group(blood_group)

    return jsonify({
        "success": True,
        "blood_group": blood_group,
        "donors": donor_data
    })


# =====================================
# SOS ALERT ROUTE
# =====================================

@routes.route("/sos", methods=["POST"])
def sos_alert():

    data = request.json

    user_name = data.get("name")
    location = data.get("location")

    send_sos_alert(user_name, location)

    return jsonify({
        "success": True,
        "message": "🚨 SOS Alert Sent Successfully"
    })


# =====================================
# AMBULANCE REQUEST ROUTE
# =====================================

@routes.route("/ambulance", methods=["POST"])
def ambulance():

    data = request.json

    user_name = data.get("name")
    hospital_name = data.get("hospital")

    request_ambulance(user_name, hospital_name)

    return jsonify({
        "success": True,
        "message": "🚑 Ambulance Requested Successfully"
    })


# =====================================
# STATUS ROUTE
# =====================================

@routes.route("/status", methods=["GET"])
def status():

    return jsonify({
        "system": "SPAM X",
        "status": "🟢 Active",
        "services": [
            "Hospitals",
            "Ambulance",
            "Blood Donors",
            "Emergency SOS"
        ]
    })


# =====================================
# END OF FILE
# =====================================