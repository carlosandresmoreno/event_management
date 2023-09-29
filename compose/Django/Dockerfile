# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=config.settings.local

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Start Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]