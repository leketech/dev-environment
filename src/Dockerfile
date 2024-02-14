FROM python:3.10-slim
# Set the working directory in the container
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY ./requirements.txt /app/requirements.txt
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
# Copy the rest of your app's source code from your host to your image filesystem.
COPY . /app
# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 80
# Define environment variable
ENV MODULE_NAME="main"
ENV VARIABLE_NAME="app"
ENV PORT="80"
# Run the application:
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

#CMD uvicorn $MODULE_NAME:$VARIABLE_NAME --host 0.0.0.0 --port $PORT