This project is a simple Django application that serves as the backend for a React.js frontend. It provides a couple of API endpoints that can be consumed by the React app.

## Features

- **API Endpoints**:
  - `/api/message/`: Returns a simple greeting message.
  - `/api/data/`: Returns a JSON object with user data.
 
## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.6 or later.
- You have installed `pip`.
- You have installed `git`.

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/raghubanshi/simple-django-app.git
cd simple-django-app
```
### 2. Create a Virtual Environment

```sh
python3 -m venv venv
source venv/bin/activate
cd mydjangoapp
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Run the Development Server

```sh
python manage.py runserver
```

## API Endpoints
URL: `/api/message/` /n
Method: `GET`
Response:
```
{
  "message": "Hello from Django!"
}
```
URL: `/api/data/`
Method: `GET`
Response:
```
{
  "name": "Praveen Raghubanshi",
  "age": 25,
  "city": "St Louis"
}
```
