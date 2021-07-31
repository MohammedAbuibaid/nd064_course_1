# Go Hello World

This is a simple Go web application that prints a "Hello World" message.

## Run the application

This application listens on port `6111`

To run the application, use the following command:
```
go run main.go 
```

Access the application on: http://127.0.0.1:6111/

To build tag and push the image to DockerHub, use the following commands:

# build the image
docker build -t go-helloworld .

# run the container
docker run -d -p 6111:6111 go-helloworld

# tag the image
docker tag go-helloworld maabuibaid/go-helloworld:v1.0.0

# push the image
docker push maabuibaid/go-helloworld:v1.0.0

