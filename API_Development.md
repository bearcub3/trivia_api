# API Develoopment and Documentation (ADD)

## What are APIs?

Application Programing Interface

- It doesn't expose application implementation to those who shouldn't have access to it. (controlled exposure of your application and data)
- The API provides a standar way of accessing the application.
- It makes it much easier to understand how to access the application's data.

### Client-Server Communication

API is intermediary/interface to deal with what client requests to deliver.

Here is the process listed out:
1. Client sends a request to the API server
2. The API server parses that request
3. Assuming the request is formatted correctly, the server queries the database for the information or performs the action in the request
4. The server formats the response and sends it back to the client
5. The client renders the response according to its implementation

### Internet Protocols (IPs)

Internet Protocol (IP) is the protocol for sending data from one computer to another across the internet. Each computer must have a unique IP address that identifies it from all other computers connected to the internet. 

There are many other internet protocols including:
* Transmission Control Protocol (TCP) which is used for data transmission
* HyperText Transmission Protocol (HTTP) which is used for transmitting **text** and **hyperlinks**
* File Transfer Protocol (FTP) which is used to transfer files between server and client

## RESTful APIs

- **Respresentational State Transfer**
- Architectural style employed by RESTful APIs
- Introduced by Roy Fielding in his dissertation in 2000
- Defined by key principles

1. Uniform Interface
Every rest architecture must have a standardized way of accessing and processing data resources. This include unique resource identifiers (i.e., unique URLs) and self-descriptive messages in the server response that describe how to process the representation (for instance JSON vs XML) of the data resource.

2. Stateless
Every client request is self-contained in that the server doesn't need to store any application data in order to make subsequent requests

3. Client-Server
There must be both a client and server in the architecture

4. Cacheable & Layered System
Caching and layering increases networking efficiency


## Introduction to HTTP

**Hypertext Transfer Protocol(HTTP)** is a protocol that provides a standardized way for computers to communicate with each other. It has been the foundation for data communication over the internet since 1990 and is integral to understanding how client-server communication functions.


Elements:    
- Uniform Resource Identifier(URIs)
- Messages : Requests and Responses
- Status Codes (e.g. 404 NOT Found)    

Features:    
* Connectionless: When a request is sent, the client opens the connection; once a response is received, the client closes the connection. The client and server only maintain a connection during the response and request. Future responses are made on a new connection.
* Stateless: There is no dependency between successive requests.
* Not Sessionless: Utilizing headers and cookies, sessions can be created to allow each HTTP request to share the same context.
* Media Independent: Any type of data can be sent over HTTP as long as both the client and server know how to handle the data format. In our case, we'll use JSON.

Elements:
* Universal Resource Identifiers (URIs): An example URI is `http://www.example.com/tasks/term=homework`. It has certain components:
    * Scheme: specifies the protocol used to access the resource, HTTP or HTTPS. In our example http.
    * Host: specifies the host that holds the resources. In our example www.example.com.
    * Path: specifies the specific resource being requested. In our example, /tasks.
    * Query: an optional component, the query string provides information the resource can use for some purpose such as a search parameter. In our example, /term=homework.

```
Side Note: URI vs URL
The term URI can refer to any identifier for a resource—for example,
it could be either the name of a resource or the address of a resource (since both the name and address are identifiers of that resource).
In contrast, URL only refers to the location of a resource—in other words, it only ever refers to an address.

So, "URI" could refer to a name or an address, while "URL" only refers to an address.
Thus, URLs are a specific type of URI that is used to locate a resource on the internet when a client makes a request to a server.
```

### HTTP Requests

Elements:     
- Method `GET https://www.example.com/task?term=homework`
- Path   `HTTP/2.0`
- HTTP Version `Accept-Language: en`
- Headers (optional)
- Body (optional)

### HTTP request methods

Elements:    
- Method: Defines the operation to be performed, such as, `GET, POST, PUT, PATCH, DELETE, OPTIONS`
- Path: The URL of the resource to be fetched, excluding the scheme and host
- HTTP Version
- Headers: optional information, success as Accept-Language
- Body: optional information, usually for methods such as POST and PATCH, which contain the resource being sent to the serve

### HTTP Responses

Elements:    
- HTTP Version        `HTTP/2.0 200 OK`
- Status Code         `Date: Fri, 21 June 2019 16:17:18 GMT`
- Headers(optional)   `Content-Type: text/html`
- Body(optional)      `Accept-Ranges: bytes`

### HTTP Status Codes

Code Category:    
- 1xx informational
- 2xx success
- 3xx redirection
- 4xx client error
- 5xx server error

Elements:    
- Status Code & Status Message
- HTTP Version
- Headers: similar to the request headers, provides information about the response and resource representation. Some common headers include:
    * Date
    * Content-Type: the media type of the body of the request
- Body: optional data containing the requested resource

