# api-gateway
This project is to show an architecture using micro services and restful apis.

# Microservices
This project creates api end points for every individual model (with maybe the exception of the ManyToMany mapping ones). In order for the end points to be accessed an `Authrization: Bearer <token>` or `grant_type: client_credentials` header needs to be sent. They both have a very distinct purpose. The Bearer access token is mean for the end users where as the client_credientials is meant for our app to do very app specific things. (I.e. Enter users` details in our system, generate auth tokens).

# Gateway
This is the app the end user talks to via the web requests. 
The real purpose of this project is to store the API tokens needed for authentication  in the session. This is to prevent people from screwing around with the api end point. The Microservice server is locked down tight so only the gatewate server has direct access to to communicate with it. Any other requests should be denied without hesitation.
