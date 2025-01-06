from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Sample data
DESTINATIONS = [
    {
        "name": "Paris",
        "attractions": ["Eiffel Tower", "Louvre Museum", "Notre Dame", "Montmartre", "Versailles"]
    },
    {
        "name": "Tokyo",
        "attractions": ["Tokyo Tower", "Shinjuku Gyoen", "Asakusa Temple", "Akihabara", "Meiji Shrine"]
    },
    {
        "name": "New York",
        "attractions": ["Statue of Liberty", "Central Park", "Times Square", "Empire State Building", "Brooklyn Bridge"]
    }
]

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/destination/<name>', methods=['GET'])
def destination_details(name):
    dest_data = next((d for d in DESTINATIONS if d['name'].lower() == name.lower()), None)
    if not dest_data:
        return jsonify({"error": "Destination not found"}), 404

    insights = {
        "cultural_tips": "Be respectful of local customs and traditions.",
        "transport": "Public transport is efficient and affordable.",
        "dining": "Try the local cuisine for an authentic experience."
    }
    
    return jsonify({"destination": name, "details": dest_data, "insights": insights})

@app.route('/create_itinerary', methods=['POST'])
def create_itinerary():
    data = request.json
    destination = data.get("destination")
    try:
        days = int(data.get("days", 1))
    except ValueError:
        return jsonify({"error": "Invalid number of days provided"}), 400

    dest_data = next((d for d in DESTINATIONS if d['name'].lower() == destination.lower()), None)
    if not dest_data:
        return jsonify({"error": "Destination not found"}), 404

    itinerary = []
    attractions = random.sample(dest_data["attractions"], min(len(dest_data["attractions"]), days))
    for day, attraction in enumerate(attractions, start=1):
        itinerary.append({"day": day, "activity": attraction})

    return jsonify({"destination": destination, "itinerary": itinerary})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get("message", "").lower()
    responses = {
        "tell me about paris": "Paris is known as the city of lights. Must-visit attractions include the Eiffel Tower and Louvre Museum.",
        "recommend food in tokyo": "Try sushi, ramen, and tempura for an authentic Tokyo experience.",
        "how do i get around new york": "Use the subway or yellow taxis for convenient travel in New York."
    }
    response = responses.get(message, "Sorry, I don't have information on that.")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
