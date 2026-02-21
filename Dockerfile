# Use official Python 3.11 image
FROM python:3.11-slim

# Set working directory
WORKDIR /usr/src/app

# Copy requirements (Flask)
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port
EXPOSE 5000

# Use Python to run your app directly
CMD ["python", "app.py"]