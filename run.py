
from app.routes import app  # Import the Flask app instance

if __name__ == "__main__":
    # Run the Flask app on default port 5000
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print("Exception occurred while starting Flask:", e)
