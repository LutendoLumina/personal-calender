# Personal Calendar App

A full-stack, Google Calendar–inspired personal calendar application built with **Django**, **PostgreSQL**, and **React**.  
This project focuses on backend fundamentals such as authentication, date/time logic, data ownership, and secure configuration using environment variables.

---

## 🚀 Project Overview

This application allows users to create, view, update, and delete personal calendar events in a clean and simple interface.  
Each user has a private calendar, and the system prevents overlapping events to avoid scheduling conflicts.

The project is designed as a **portfolio-quality backend-focused application**, following real-world development practices.

---

## 🎯 Project Goals

This project was built to:

- Practice real-world backend development using Django
- Learn how to handle date and time logic correctly
- Understand user authentication, permissions, and data ownership
- Build a complete CRUD-based application from scratch
- Use PostgreSQL in a production-style setup
- Secure sensitive configuration using environment variables
- Create a job-ready portfolio project

---

## 👤 Target Users

This project is suitable for:

- Students managing classes, assignments, and study schedules
- Job seekers tracking interviews and deadlines
- Professionals planning meetings and personal events
- Individuals who want a simple, private calendar

The app is focused on **individual users**, not teams.

---

## ✨ Features (Current)

- User authentication (Django built-in system)
- Personal event creation
- Monthly calendar view (backend-ready)
- Event editing and deletion
- Event ownership (users can only access their own events)
- PostgreSQL database integration
- Secure secret management using `.env`
- Admin interface for managing users and events

---

## 🧱 Tech Stack

### Backend
- **Python**
- **Django**
- **PostgreSQL**
- **psycopg2-binary**
- **python-dotenv**

### Frontend (Planned)
- **React**

### DevOps / Tooling
- Git & GitHub
- Virtual environments (venv)
- Environment variables
- Docker (planned)
- Deployment (planned: Render / Fly.io / Vercel)

---

## 📁 Project Structure

personal-calender/
├── manage.py
├── .env
├── backend/                 
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── events/                   
│ ├── models.py
│ ├── admin.py
│ └── migrations/
├── .venv/
├── .gitignore
└── README.md


---

## 🗄️ Data Models

### User
Uses Django’s built-in `User` model for authentication and permissions.

### Event
Represents a single calendar event.

Fields:
- `user` (ForeignKey to User)
- `title`
- `date`
- `start_time`
- `end_time`
- `created_at`
- `updated_at`

Each event belongs to **one user**, and users cannot see each other’s events.

---

## 🔐 Environment Variables

Sensitive configuration is stored in a `.env` file (not committed to GitHub).

Example `.env`:

DJANGO_SECRET_KEY=your_secret_key_here

DB_NAME=calendar_db
DB_USER=calendar_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

---

## 🛠️ Setup Instructions (Local Development)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/personal-calendar.git
cd personal-calendar
```

### 2. Create and activate virtual enviroment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure enviroment variables
Create a `.env` file in the project root and add rewuired values.

### 5. Run database migrations
```bash
python manage.py migrate
```

### 6. Create admin user
```bash
python manage.py createsuperuser
```

### 7. Start development server
```bash
python manage.py runserver
```

---

## 🧪 Admin Panel

Access the Django admin panel at:

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

From here you can:

- Manage users
- Create, edit, and delete events
- Inspect database records

---

## 🔮 Planned Features

- Event conflict detection (overlapping events)
- REST API using Django REST Framework
- React frontend with calendar UI
- Google Calendar API integration
- Event categories and reminders
- Deployment with Docker
- Production hosting

---

## 📌 Development Status

🟡 **In Progress**

### Current Phase

- Backend setup and configuration
- Database integration with PostgreSQL
- Core data models implemented

## ✅ Step 2: Database & Data Models

- PostgreSQL installed and configured
- Django connected to PostgreSQL using environment variables
- `Event` model implemented
- Database migrations applied
- CRUD operations verified using Django admin

## ⏳ Step 3: Backend API

- Design REST API endpoints for event management
- Implement authentication-protected routes
- Restrict data access to event owners
- Prepare backend for React frontend integration

Frontend and API layers will be added in later phases.


---

## 🧪 API Testing

All backend API endpoints have been tested using **Django REST Framework’s Browsable API** during development.

The following scenarios were verified:

- User authentication using Django session-based auth
- Fetching events for the authenticated user (`GET /api/events/`)
- Creating new events (`POST /api/events/`)
- Updating existing events (`PUT /api/events/<id>/`)
- Deleting events (`DELETE /api/events/<id>/`)
- Input validation (end time must be after start time)
- Event conflict detection (prevention of overlapping events)
- Data isolation (users cannot view or modify other users’ events)

Testing was performed while logged in to ensure permissions, ownership checks, and business logic behave correctly.

### 🔍 Testing Tool Used

- **Django REST Framework – Browsable API**

This tool enabled interactive inspection of requests and responses directly in the browser without relying on external API clients.









