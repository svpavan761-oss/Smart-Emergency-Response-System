# =====================================
# SPAM X - database.py
# Smart Emergency Response System
# =====================================

import json
import os


# -------------------------------------
# FILE PATHS
# -------------------------------------

USERS_FILE = "../database/users.json"
HOSPITALS_FILE = "../database/hospitals.json"
DONORS_FILE = "../database/donors.json"


# -------------------------------------
# LOAD JSON DATA
# -------------------------------------

def load_data(file_path):

    try:

        with open(file_path, "r") as file:

            data = json.load(file)

            return data

    except FileNotFoundError:

        print(f"❌ File not found: {file_path}")

        return []

    except json.JSONDecodeError:

        print(f"❌ Invalid JSON format in {file_path}")

        return []


# -------------------------------------
# SAVE JSON DATA
# -------------------------------------

def save_data(file_path, data):

    with open(file_path, "w") as file:

        json.dump(data, file, indent=4)

    print(f"✅ Data saved successfully to {file_path}")


# -------------------------------------
# USERS FUNCTIONS
# -------------------------------------

def get_all_users():

    return load_data(USERS_FILE)


def add_user(user):

    users = load_data(USERS_FILE)

    users.append(user)

    save_data(USERS_FILE, users)

    print("✅ User added successfully!")


def find_user_by_email(email):

    users = load_data(USERS_FILE)

    for user in users:

        if user["email"] == email:

            return user

    return None


# -------------------------------------
# HOSPITAL FUNCTIONS
# -------------------------------------

def get_all_hospitals():

    return load_data(HOSPITALS_FILE)


def get_available_hospitals():

    hospitals = load_data(HOSPITALS_FILE)

    available = []

    for hospital in hospitals:

        if hospital["status"] == "Available":

            available.append(hospital)

    return available


# -------------------------------------
# DONOR FUNCTIONS
# -------------------------------------

def get_all_donors():

    return load_data(DONORS_FILE)


def find_donors_by_blood_group(blood_group):

    donors = load_data(DONORS_FILE)

    matching_donors = []

    for donor in donors:

        if donor["blood_group"] == blood_group:

            matching_donors.append(donor)

    return matching_donors


# -------------------------------------
# LOGIN VALIDATION
# -------------------------------------

def validate_login(email, password):

    users = load_data(USERS_FILE)

    for user in users:

        if user["email"] == email and user["password"] == password:

            return True

    return False


# -------------------------------------
# TESTING
# -------------------------------------

if __name__ == "__main__":

    print("\n========== USERS ==========\n")

    users = get_all_users()

    print(users)


    print("\n====== AVAILABLE HOSPITALS ======\n")

    hospitals = get_available_hospitals()

    print(hospitals)


    print("\n====== O+ DONORS ======\n")

    donors = find_donors_by_blood_group("O+")

    print(donors)


    print("\n====== LOGIN CHECK ======\n")

    result = validate_login(
        "pavan@gmail.com",
        "pavan123"
    )

    print("Login Success:", result)


# =====================================
# END OF FILE
# =====================================