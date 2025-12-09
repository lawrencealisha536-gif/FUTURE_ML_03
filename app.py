from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rule-based hostel chatbot (no external API)
def hostel_bot_reply(user_text: str) -> str:
    text = user_text.lower()

    # Greetings
    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! I am the hostel assistant. How can I help you?"

    # Hostel timings
    if "timing" in text or "time" in text or "open" in text or "entry" in text or "curfew" in text:
        return "Hostel main gate entry time is 6:00 AM to 10:30 PM. Late entry requires warden permission."

    # Admission / eligibility
    if "admission" in text or "apply" in text or "eligibility" in text or "who can stay" in text:
        return "Hostel admission is for full‑time enrolled students only. You need a college ID, admission receipt, and completed hostel form."

    # Fees
    if "fee" in text or "fees" in text or "rent" in text or "charge" in text or "cost" in text:
        return "Hostel fees include room rent, mess charges and caution deposit. Exact amount depends on room type (2/3/4‑sharing)."

    # Mess / food
    if "mess" in text or "food" in text or "breakfast" in text or "lunch" in text or "dinner" in text:
        return "Mess timings are: breakfast 7:30–9:00 AM, lunch 12:30–2:00 PM, and dinner 7:30–9:00 PM. Veg meals are served daily; special menu on weekends."

    # Rules / discipline
    if "rule" in text or "discipline" in text or "policy" in text:
        return "Key rules: carry your ID card, no loud noise after 10:00 PM, visitors allowed only in common area, and strictly no ragging or alcohol."

    # Visitors
    if "visitor" in text or "parents" in text or "guardian" in text:
        return "Visitors are allowed in the visiting area from 4:00–7:00 PM with entry in the visitor register. Night stay for parents is not allowed."

    # Wi-Fi / facilities
    if "wifi" in text or "wi-fi" in text or "internet" in text or "facility" in text or "laundry" in text:
        return "Facilities include Wi‑Fi, common TV room, reading room, and paid laundry. Wi‑Fi is available from 6:00 AM to 12:00 midnight."

    # Rooms / sharing
    if "room" in text or "sharing" in text or "2 sharing" in text or "3 sharing" in text:
        return "Rooms are available in 2, 3 and 4‑sharing. Each student gets a bed, cupboard, chair and study table."

    # Complaints
    if "complaint" in text or "issue" in text or "problem" in text or "maintenance" in text:
        return "For complaints (water, electricity, room issues), please inform the caretaker or fill the maintenance form at the hostel office."

    # Emergency / contact
    if "emergency" in text or "help" in text or "contact" in text or "phone" in text:
        return "In emergency, contact the hostel warden or security guard. You can also reach the college helpline number mentioned on your ID card."

    # Ragging / safety
    if "ragging" in text or "safety" in text or "harass" in text:
        return "Ragging is strictly prohibited. You can confidentially report any incident to the warden or anti‑ragging committee."

    # Default
    return "I am a simple hostel assistant. Please ask about hostel timings, admission, fees, mess, rules, rooms, or emergency contacts."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    reply = hostel_bot_reply(user_msg)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)