FROM python:3.10-slim

# Set environment
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy app
COPY . /app

EXPOSE 5000

# Use gunicorn to serve the Flask app: app:app
ENV PORT=5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:$(PORT)", "app:app"]
