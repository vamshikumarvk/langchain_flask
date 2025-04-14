# Use official Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# GOOGLE_API_KEY environment variable
ENV GOOGLE_API_KEY=""

# Expose the port
EXPOSE 5000

# Start the Flask app
CMD ["python", "run.py"]
