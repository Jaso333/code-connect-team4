# Flask API Application

This is a simple Flask API application with endpoints to create, retrieve, and update user profiles.

## Requirements

- Python 3.6+
- Flask 2.0.1

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the Flask application:
    ```sh
    python app/app.py
    ```

2. The application will be running at `http://127.0.0.1:5000/`.

## API Endpoints

### Create a new user

- **URL:** `/users`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "bio": "A software developer with 10 years of experience.",
        "skills": ["Python", "Flask", "JavaScript"],
        "profile_picture": "http://example.com/profile.jpg",
        "github_gitlab": "http://github.com/johndoe"
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "bio": "A software developer with 10 years of experience.",
        "skills": ["Python", "Flask", "JavaScript"],
        "profile_picture": "http://example.com/profile.jpg",
        "github_gitlab": "http://github.com/johndoe"
    }
    ```

### Retrieve all users

- **URL:** `/users`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "1": {
            "name": "John Doe",
            "bio": "A software developer with 10 years of experience.",
            "skills": ["Python", "Flask", "JavaScript"],
            "profile_picture": "http://example.com/profile.jpg",
            "github_gitlab": "http://github.com/johndoe"
        }
    }
    ```

### Retrieve user profile

- **URL:** `/users/{userId}`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "name": "John Doe",
        "bio": "A software developer with 10 years of experience.",
        "skills": ["Python", "Flask", "JavaScript"],
        "profile_picture": "http://example.com/profile.jpg",
        "github_gitlab": "http://github.com/johndoe"
    }
    ```

### Update user profile

- **URL:** `/users/{userId}`
- **Method:** `PUT`
- **Request Body:**
    ```json
    {
        "name": "John Smith"
    }
    ```
- **Response:**
    ```json
    {
        "name": "John Smith",
        "bio": "A software developer with 10 years of experience.",
        "skills": ["Python", "Flask", "JavaScript"],
        "profile_picture": "http://example.com/profile.jpg",
        "github_gitlab": "http://github.com/johndoe"
    }
    ```

### Create an example user

- **URL:** `/example_user`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "bio": "A software developer with 10 years of experience.",
        "skills": ["Python", "Flask", "JavaScript"],
        "profile_picture": "http://example.com/profile.jpg",
        "github_gitlab": "http://github.com/johndoe"
    }
    ```

## API Documentation

Swagger UI is available at `http://127.0.0.1:5000/swagger`.

## Example curl commands

### Create a new user