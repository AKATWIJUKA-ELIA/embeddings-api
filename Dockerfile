
FROM python:3-slim
# Copy only requirements first
COPY requirements.txt /api/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /api/requirements.txt

# Copy the rest of the code
COPY . /api

WORKDIR /api

# Start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]