# Identify the baseimage
FROM python:alpine

WORKDIR /app

# Copy & install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the project
COPY . .

# Start the app
CMD [ "python", "app.py" ]

