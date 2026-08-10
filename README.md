# Authentication API

A simple authentication API built with FastAPI, PostgreSQL, SQLAlchemy, JWT, and Argon2 password hashing.

## Features

* User registration
* Secure password hashing with Argon2
* JWT-based authentication
* Protected user endpoint
* JWT authentication middleware
* Request/response logging
* PostgreSQL database
* Async SQLAlchemy
* Alembic database migrations
* Health check endpoint
* Interactive Swagger API documentation

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* AsyncPG
* Alembic
* PyJWT
* pwdlib + Argon2
* Uvicorn

## Project Structure

```text
app/
├── main.py
├── config.py
├── security.py
├── logging_config.py
│
├── db/
│   ├── database.py
│   └── models.py
│
├── middleware/
│   ├── auth.py
│   └── logging.py
│
└── routes/
    └── auth.py
```

## API Endpoints

| Method | Endpoint         | Description             | Authentication |
| ------ | ---------------- | ----------------------- | -------------- |
| GET    | `/`              | API status              | No             |
| GET    | `/health`        | API and database health | No             |
| POST   | `/auth/register` | Register a user         | No             |
| POST   | `/auth/login`    | Login and receive JWT   | No             |
| GET    | `/auth/me`       | Get authenticated user  | Yes            |

## Authentication Flow

```text
Register
   ↓
Hash password with Argon2
   ↓
Store user in PostgreSQL
   ↓
Login
   ↓
Verify password
   ↓
Generate JWT
   ↓
Send JWT with protected requests
   ↓
JWT Middleware validates token
   ↓
Access protected resources
```

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd auth-api
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate it on Windows Git Bash:

```bash
source .venv/Scripts/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=postgresql+asyncpg://postgres:YOUR_PASSWORD@localhost:5432/auth_api

JWT_SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Never commit `.env` to Git.

### 5. Run database migrations

```bash
alembic upgrade head
```

### 6. Start the API

```bash
uvicorn app.main:app --reload
```

### 7. Open API documentation

```text
http://127.0.0.1:8000/docs
```

## Database

The application currently uses a single `users` table:

```text
users
├── id
├── username
├── email
├── hashed_password
└── created_at
```

Passwords are never stored in plain text.

## Authentication

After successful login, the API returns a JWT access token.

Protected requests require:

```text
Authorization: Bearer <access_token>
```

## Development

Run the application:

```bash
uvicorn app.main:app --reload
```

Create a new migration after model changes:

```bash
alembic revision --autogenerate -m "describe change"
```

Apply migrations:

```bash
alembic upgrade head
```

## License

This project is intended for learning and development purposes.
