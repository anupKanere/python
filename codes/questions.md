### What is a RESTful API, and what are its core principles?

-> A RESTful API (Representational State Transfer API) is a style of software architecture that uses HTTP to enable communication between a client and a server. It is widely used to build web services that are scalable, stateless, and easy to integrate.

- Core Principles of RESTful APIs

1. Statelessness:
Each request from a client to the server must contain all the information needed to understand and process the request.
The server does not store the client's state between requests, which simplifies scalability.

2. Client-Server Separation:
The client (frontend) and the server (backend) are independent of each other.
Clients only care about the resources provided, and servers provide the resources without knowledge of how the client consumes them.

3. Resource Identification:
Resources (data objects like users, orders, etc.) are identified using URIs (Uniform Resource Identifiers).
For example:
/users represents all users.
/users/123 represents a specific user with ID 123.

4. Uniform Interface:
RESTful APIs enforce a standard set of interactions to manipulate resources:
GET: Retrieve a resource.
POST: Create a resource.
PUT or PATCH: Update a resource.
DELETE: Remove a resource.
This uniformity improves API simplicity and predictability.

5. Representation of Resources:
Resources can be represented in various formats, such as JSON, XML, or HTML.
JSON is the most common format due to its simplicity and ease of use.

6. Stateless Communication Using HTTP:
HTTP methods are used for communication.
Status codes (e.g., 200 OK, 404 Not Found, 201 Created) are used to inform the client about the result of their request.

7. Cacheability:
Responses must define whether they are cacheable or not to improve performance.
Proper use of HTTP caching headers (Cache-Control, Expires, etc.) can enhance efficiency.

8. Layered System:
A client does not need to know whether it is directly communicating with the server or an intermediary (e.g., load balancer, proxy).
This abstraction enhances scalability and reliability.

9. Code on Demand (Optional):
Servers can send executable code (e.g., JavaScript) to the client when required.
This principle is optional and is not commonly used.

