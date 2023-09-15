## FastAPI API Documentation

**Version:** 0.1.0

### Endpoints

- **Index**
  - **Summary:** Retrieve index information.
  - **HTTP Method:** GET
  - **Path:** `/`
  - **Responses:**
    - **200:** Successful Response (Content: JSON)
    
- **Create User**
  - **Summary:** Create a new user.
  - **HTTP Method:** POST
  - **Path:** `/api`
  - **Request Body:** PersonCreate JSON object (Required)
  - **Responses:**
    - **200:** Successful Response (Content: Person JSON object)
    - **422:** Validation Error (Content: HTTPValidationError JSON object)

- **Get User**
  - **Summary:** Retrieve user information by name.
  - **HTTP Method:** GET
  - **Path:** `/api/user_id`
  - **Query Parameter:**
    - `name` (string, required): Name of the user
  - **Responses:**
    - **200:** Successful Response (Content: JSON)
    - **422:** Validation Error (Content: HTTPValidationError JSON object)

- **Delete User**
  - **Summary:** Delete a user by name.
  - **HTTP Method:** DELETE
  - **Path:** `/api/user_id`
  - **Query Parameter:**
    - `name` (string, required): Name of the user
  - **Responses:**
    - **200:** Successful Response (Content: JSON)
    - **422:** Validation Error (Content: HTTPValidationError JSON object)

- **Update User**
  - **Summary:** Update user information by name.
  - **HTTP Method:** PUT
  - **Path:** `/api/user_id`
  - **Query Parameter:**
    - `name` (string, required): Name of the user to update
  - **Request Body:** PersonCreate JSON object (Required)
  - **Responses:**
    - **200:** Successful Response (Content: Person JSON object)
    - **422:** Validation Error (Content: HTTPValidationError JSON object)

### Data Schemas

- **Person**
  - Properties:
    - `name` (string, required): Name of the user
    - `id` (integer): User ID
    - `createdAt` (string): Creation timestamp
    - `updatedAt` (string): Last update timestamp

- **PersonCreate**
  - Properties:
    - `name` (string, required): Name of the user

- **HTTPValidationError**
  - Properties:
    - `detail` (array of ValidationError): Validation error details
      - `loc` (array of strings/integers): Location of the error
      - `msg` (string): Error message
      - `type` (string): Error type

- **ValidationError**
  - Properties:
    - `loc` (array of strings/integers): Location of the error
    - `msg` (string): Error message
    - `type` (string): Error type

This documentation provides information about the available API endpoints, their descriptions, request/response formats, and data schemas.
