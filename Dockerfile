# Use an official Python image
FROM python:3.9.6
 
# Set working directory
WORKDIR /app

# Set environment variables
ENV FLASK_RUN_HOST=0.0.0.0
ENV GOOGLE_API_KEY="AIzaSyD71MdPeL2jqv9M-vgK8Jgk2ex_jNYWLBU"

# Copy files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose port
EXPOSE 5000

# Run the app
CMD ["flask", "run"]
