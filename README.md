**AI-Powered Travel Itinerary Planner:** 
A smart, AI-driven travel assistant that simplifies trip planning by creating personalized day-by-day itineraries. Whether you're a solo traveler, a family, or a group of friends, our tool ensures every trip is tailored to your preferences, offering curated attractions, cultural tips, and essential travel insights.

**Features**
Personalized Itinerary: Generate custom itineraries based on your selected destination and number of days.
Destination Insights: Get key information about local attractions, cultural tips, transport options, and dining recommendations.
Interactive Chatbot: Ask questions about destinations, food, or travel tips and get instant responses.
Simple and Intuitive Interface: User-friendly design for seamless travel planning.

**Tech Stack**
Backend: Flask (Python)
Frontend: HTML, CSS, JavaScript
APIs & Libraries: Random module for itinerary generation, Flask for routing and server setup
Database: Sample in-memory data for destinations

**How to Run the Project**
1. Clone the Repository
            git clone https://github.com/aakriti1613/Travel-Itinerary-Planner.git  
            cd Travel-Itinerary-Planner  
2. Install Dependencies
Ensure you have Python installed. Then, install Flask:
            pip install flask
3. Run the Application
            python myapp.py
4. Access the App
Open your browser and navigate to http://127.0.0.1:5000/.

**Endpoints**
Home: Displays the landing page (/).
Destination Details: Fetches details of a specific destination (/destination/<name>).
Create Itinerary: Generates a custom itinerary (/create_itinerary, POST).
Chatbot Interaction: Handles chatbot queries (/chat, POST).

**Preview**
![Travel Itinerary Planner - Google Chrome 1_2_2025 11_07_03 PM](https://github.com/user-attachments/assets/ebf295fe-5801-48e5-9873-2103ba1d8dae)
![Travel Itinerary Planner - Google Chrome 1_2_2025 11_07_25 PM](https://github.com/user-attachments/assets/af485c34-352d-403d-9da8-67466d035f8f)

**Future Enhancements**
Integration with live APIs for real-time weather updates, flight bookings, and transport options.
Collaboration features for group trip planning.
Eco-friendly travel suggestions and budget optimization tools.
Enhanced chatbot with multilingual support and voice interaction.

**Contributing**
Contributions are welcome! 
