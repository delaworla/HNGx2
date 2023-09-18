# Person REST API

This project implements a simple REST API for managing "person" resources, including creating, reading, updating, and deleting person records. The API is developed using FastAPI and can interface with any chosen database. It also dynamically handles parameters, allowing you to perform operations based on user-provided input, such as a person's name.

## Table of Contents

- [Person REST API](#person-rest-api)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
    - [Creating a New Person](#creating-a-new-person)
    - [Fetching Person Details](#fetching-person-details)
    - [Updating Person Details](#updating-person-details)
    - [Deleting a Person](#deleting-a-person)
  - [Database Modeling (Bonus)](#database-modeling-bonus)
  - [Testing](#testing)
  - [Dynamic Parameter Handling](#dynamic-parameter-handling)
  - [Documentation](#documentation)
  - [GitHub Repository] (#github-repository)
  - [Hosting] (#hosting)
  - [Acceptance Criteria] (#acceptance-criteria)

## Features

- **CRUD Operations:** The API supports basic CRUD operations (Create, Read, Update, Delete) on person resources.
- **Secure Database Interaction:** Interactions with the database are secure and protected against common vulnerabilities such as SQL injections.
- **Dynamic Parameter Handling:** The API can process operations based on user-provided parameters, such as a person's name.
- **Detailed Documentation:** A comprehensive documentation file outlines request/response formats, setup instructions, and sample API usage.

## Getting Started

### Prerequisites

Before running the API, you need the following prerequisites:

- Python (3.7+)
- FastAPI (installed automatically)

### Installation

1. Clone the GitHub repository to your local machine:

   ```bash
   git clone https://github.com/delaworla/HNGx2.git
   cd HNG_CRUD

   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
    python -m venv venv
    source venv/bin/activate

   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the application

```bash
uvicorn src.main:app --reload
```

### Creating a New Person

To create a new person, send a POST request to `/api` with a JSON body containing the person's name.

**Example Request:**

```
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe"}' http://localhost:8000/api
```

### Fetching Person Details

To fetch details of a person by name, send a GET request to `/api/user_id` with the `name` query parameter.

**Example Request:**

```
curl http://localhost:8000/api/user_id?name=John%20Doe
```

### Updating Person Details

To update a person's details by name, send a PUT request to `/api/user_id` with the `name` query parameter and a JSON body containing the updated information.

**Example Request:**

```
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Jane Doe"}' http://localhost:8000/api/user_id?name=John%20Doe
```

### Updating Person Details

To update a person's details by name, send a PUT request to `/api/user_id` with the `name` query parameter and a JSON body containing the updated information.

**Example Request:**

```
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Jane Doe"}' http://localhost:8000/api/user_id?name=John%20Doe
```

### Deleting a Person

To delete a person by name, send a DELETE request to `/api/user_id` with the `name` query parameter.

**Example Request:**

```
curl -X DELETE http://localhost:8000/api/user_id?name=Jane%20Doe
```

### Testing

Testing the API can be done using tools like Postman or by writing scripts in Python using the requests library. You should test each CRUD operation:

1. Adding a new person (e.g., "Mark Essien").
2. Fetching details of a person.
3. Modifying the details of an existing person.
4. Removing a person.

```
pytest
```

### Database Modeling (Bonus)

As a bonus feature, we provide a UML diagram representing the database structure and relationships. Please refer to the provided diagram for a visual representation of the database schema and how different entities are related.

### Dynamic Parameter Handling

The API is flexible and can handle dynamic input. You can provide a name (or other details) to perform operations using that name. For example, if you pass "Mark Essien," you can perform all CRUD operations on "Mark Essien."

### Documentation

For detailed documentation on the API, including:

- Standard formats for requests and responses for each endpoint.
- Sample usage of the API.
- Any known limitations or assumptions made during development.
- Instructions for setting up and deploying the API locally or on a server.

Please refer to the [DOCUMENTATION](DOCUMENTATION.md) file.

```

```
