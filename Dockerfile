FROM python:3.6-alpine

# Create work dir /opt
RUN mkdir /opt

# Set the working directory to /opt
WORKDIR /opt

# Copy the current directory contents into the container at /opt
ADD .  /opt

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r /opt/requirements.txt

# Define environment variable
ENV NAME reverse

# Run app.py when the container launches
CMD ["python", "reverse_string_py3.py"]
