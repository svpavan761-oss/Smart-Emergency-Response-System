# =====================================
# SPAM X - emergency.py
# Smart Emergency Response System
# =====================================

from datetime import datetime


# -------------------------------------
# SOS ALERT FUNCTION
# -------------------------------------

def send_sos_alert(user_name, location):

    print("\n🚨 EMERGENCY ALERT ACTIVATED 🚨")

    print(f"User Name : {user_name}")
    print(f"Location  : {location}")

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"Time      : {current_time}")

    print("\n✅ Emergency services notified successfully!\n")


# -------------------------------------
# AMBULANCE REQUEST FUNCTION
# -------------------------------------

def request_ambulance(user_name, hospital_name):

    print("\n🚑 Ambulance Request Processing...\n")

    print(f"Patient Name : {user_name}")
    print(f"Assigned Hospital : {hospital_name}")

    print("\n✅ Ambulance dispatched successfully!\n")


# -------------------------------------
# EMERGENCY CONTACT FUNCTION
# -------------------------------------

def notify_emergency_contacts(contact_list):

    print("\n📞 Sending alerts to emergency contacts...\n")

    for contact in contact_list:

        print(f"Alert sent to: {contact}")

    print("\n✅ All emergency contacts notified!\n")


# -------------------------------------
# BLOOD DONOR REQUEST FUNCTION
# -------------------------------------

def request_blood_donor(blood_group):

    print(f"\n🩸 Searching blood donors for group {blood_group}...\n")

    print("✅ Matching donors found nearby!\n")


# -------------------------------------
# HOSPITAL STATUS FUNCTION
# -------------------------------------

def hospital_status(hospital_name, beds_available):

    print(f"\n🏥 Hospital: {hospital_name}")

    print(f"Available Beds: {beds_available}")

    if beds_available > 5:

        print("✅ Beds Available\n")

    else:

        print("⚠ Limited Beds Available\n")


# -------------------------------------
# LIVE LOCATION FUNCTION
# -------------------------------------

def detect_location(latitude, longitude):

    print("\n📍 User Location Detected")

    print(f"Latitude  : {latitude}")
    print(f"Longitude : {longitude}")

    print("\n✅ Location tracking active!\n")


# -------------------------------------
# EMERGENCY LOG FUNCTION
# -------------------------------------

def save_emergency_log(user_name, emergency_type):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = f"""
=============================
SPAM X Emergency Log
=============================
User Name      : {user_name}
Emergency Type : {emergency_type}
Time           : {current_time}
=============================
"""

    print(log)


# -------------------------------------
# TESTING FUNCTIONS
# -------------------------------------

if __name__ == "__main__":

    send_sos_alert("Pavan SV", "Mysore")

    request_ambulance("Abhishek", "Apollo Hospital")

    notify_emergency_contacts([
        "9876543210",
        "9123456780"
    ])

    request_blood_donor("O+")

    hospital_status("City Emergency Care", 8)

    detect_location(12.2958, 76.6394)

    save_emergency_log("Subhasa", "Road Accident")


# =====================================
# END OF FILE
# =====================================