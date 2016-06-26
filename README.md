# api-gateway
This project is to show an architecture using micro services and restful apis.

# Microservices
This project creates api end points for every individual model. In order for the end points to be accessed an `Authrization: Bearer <token>` or `grant_type: client_credentials` header needs to be sent

# Project
This is the app the end user talks to via the web requests. The real purpose of this project is to store the API tokens needed for authentication 
serverside to prevent people from screwing around with the api end point.
