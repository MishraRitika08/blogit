# BlogIt – Full-Stack Blogging Platform 

BlogIt is a full-stack blogging application built using **Django, Django REST Framework, PostgreSQL, HTML and Bootstrap 5**.

It provides a platform where users can create and manage blog posts, interact through comments, organize content using tags, and access blog operations through RESTful APIs.

## Live Demo

🚀 [View BlogIt Live](https://blogit-kg88.onrender.com/)

📚 [API Documentation](https://blogit-kg88.onrender.com/api/docs/)

## Features

- **User Authentication:** User registration, login and logout using Django authentication.
- **Blog Management:** Create, read, update and delete blog posts.
- **Authorization:** Only authenticated users can create posts, and only post authors can modify or delete their content.
- **Comments:** Users can interact with blog posts through comments.
- **Tag Management:** Organize blog posts using tags.
- **Image Uploads:** Attach images to blog posts.
- **RESTful APIs:** Implemented using Django REST Framework and ModelViewSet.
- **API Permissions:** Custom object-level permissions to enforce author-based access control.
- **API Documentation:** Interactive API documentation using Swagger UI and OpenAPI.
- **Pagination:** Paginated API responses and blog listings.
- **Database Management:** Relational database design using PostgreSQL.

## Tech Stack

| Category | Technologies |
|---|---|
| Backend | Python, Django |
| API Development | Django REST Framework |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Database | PostgreSQL |
| API Documentation | Swagger UI, drf-spectacular, OpenAPI |
| Authentication | Django Authentication System |
| Deployment | Render, Gunicorn, WhiteNoise |
| Version Control | Git, GitHub |

## Project Structure

```text
BlogIt/
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── api_views.py
│   ├── api_urls.py
│   └── permissions.py
│
├── users/
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── config/
│   ├── settings.py
│   └── urls.py
│
├── templates/
├── manage.py
└── requirements.txt
```

## Database Models

The application uses Django ORM with PostgreSQL.

- **User:** Django's built-in user model for authentication.
- **Post:** Stores blog title, content, author, timestamps, image and associated tags.
- **Comment:** Stores comments associated with blog posts and their authors.
- **Tag:** Stores tags used to categorize posts.
- **AIGenerationHistory:** Model for storing AI generation history; the complete AI generation workflow is planned for a future version.

### Database Relationships

- User → Post: One-to-Many
- Post → Comment: One-to-Many
- Post → Tag: Many-to-Many
- User → AIGenerationHistory: One-to-Many

## REST API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/api/posts/` | Retrieve all posts |
| POST | `/api/posts/` | Create a post |
| GET | `/api/posts/{id}/` | Retrieve a specific post |
| PUT | `/api/posts/{id}/` | Update a post |
| PATCH | `/api/posts/{id}/` | Partially update a post |
| DELETE | `/api/posts/{id}/` | Delete a post |

## API Documentation

Interactive API documentation is available through Swagger UI.

- API Schema: `/api/schema/`
- Swagger UI: `/api/docs/`

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/MishraRitika08/blogit.git
cd blogit
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory.

```env
SECRET_KEY=your_django_secret_key
DEBUG=True

DB_NAME=blogit_db
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## Future Enhancements

- GenAI-powered blog title, summary and tag generation.
- AI generation history and content management.
- Semantic search using text embeddings.
- Improved automated testing and API coverage.

## Author

**Ritika Mishra**

[GitHub](https://github.com/MishraRitika08)

