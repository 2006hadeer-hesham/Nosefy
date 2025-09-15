from flask import Flask, jsonify
import random

app = Flask(__name__)

names = [
    "Sara Mohamed", "Ahmed Ali", "Mona Khaled", "Khaled Abdelrahman", "Laila Hassan",
    "Mohamed Sameer", "Norhan Emad", "Tarek Yousry", "Doaa Kamal", "Amr Mahmoud",
    "Hoda Adel", "Yasser Fouad", "Mariam Saeed", "Shaimaa Awad", "Alaa Nasr",
    "Eman Gamal", "Fatma Zakaria", "Sameh Youssef", "Heba Morsi", "Mahmoud Hussein"
]

specializations = [
    "Critical Care Nursing", "Pediatric Nursing", "Surgical Nursing",
    "Internal Medicine Nursing", "Emergency Nursing", "Home Nursing"
]

universities = [
    "Cairo University", "Ain Shams University", "Alexandria University",
    "Assiut University", "Al-Azhar University", "Mansoura University"
]

hospitals = [
    "Salam International Hospital", "Kasr Al Ainy Hospital", "Dar Al Fouad Hospital",
    "Cleopatra Hospital", "Maadi Military Hospital", "Behman Hospital"
]

details_examples = [
    "Experienced in ICU and CPR.",
    "Specialized in newborn and pediatric care.",
    "Wide experience in emergency cases.",
    "Excellent at handling modern medical equipment.",
    "Certified in first aid and home care.",
    "Worked with elderly and Alzheimer's patients."
]

about_examples = [
    "Passionate about helping patients and improving care quality.",
    "Committed to providing respectful and humane service.",
    "Reliable and highly skilled nurse.",
    "Believes empathy is key to quality care.",
    "Works hard to create a safe and comfortable environment for patients."
]

def generate_nurse(id):
    return {
        "id": id,
        "name": names[id - 1],
        "specialization": random.choice(specializations),
        "university": random.choice(universities),
        "years_of_experience": random.randint(1, 15),
        "details": random.choice(details_examples),
        "available": random.choice([True, False]),
        "can_stay_overnight": random.choice([True, False]),
        "about": random.choice(about_examples),
        "public_data": random.choice([True, False]),
        "service_price": {
            "per_hour": random.randint(100, 250),
            "per_visit": random.randint(200, 500)
        },
        "hospital_name": random.choice(hospitals)
    }

nurses_data = {i + 1: generate_nurse(i + 1) for i in range(20)}

@app.route("/api/nurses", methods=["GET"])
def get_nurses():
    return jsonify(nurses_data)

if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/api/nurses", methods=["GET"])
# def get_nurses():
#     return jsonify(nurses_data)
