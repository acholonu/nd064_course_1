# Think of containers as copying your work environment for
# an application you are building.  And put it into the cloud to run.
# An API layer allows you to communicate between application/containers.
# Step 1: What image is this template based on
FROM golang:alpine

# Step 2: Adding Metadata. Just a key-value pair that I want to include
LABEL maintainer="UgochiJ"
LABEL creation_date="7/9/2021"

# Step 3: Setting the working directory in the container.  
WORKDIR /go/src/app

# Step 4: Adding files from my local machine (in the current directory) to the containers file system (/go/src/app)
# I could just used a period for the destination, since the container's working directory has been set.
ADD . /go/src/app

# Step 5: Building the binary
# -o means output
RUN go build  -o helloworld

# Step 6: Telling the app what port to listen on
EXPOSE 6111

# Step 7: The command to start the binary that we build
CMD ["./helloworld"]