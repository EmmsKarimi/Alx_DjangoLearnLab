# Advanced API Project - Books API

## Overview
This API allows users to manage books, supporting CRUD operations with authentication-based access control.

## Endpoints

| Method | URL                      | Description                  | Permissions       |
|--------|--------------------------|------------------------------|------------------|
| GET    | `/books/`                | Retrieve all books           | Public          |
| GET    | `/books/<int:pk>/`       | Retrieve a specific book     | Public          |
| POST   | `/books/create/`         | Create a new book            | Authenticated   |
| PUT    | `/books/<int:pk>/update/`| Update an existing book      | Authenticated   |
| DELETE | `/books/<int:pk>/delete/`| Delete a book                | Authenticated   |

## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/Alx_DjangoLearnLab.git
   cd advanced-api-project
