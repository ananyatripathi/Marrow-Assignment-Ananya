# Movies Upload and Query API

This Flask application provides a REST API for uploading movie data from a CSV file into a SQLite database. It allows users to query the stored movie data with various filtering and sorting options.

## Features

- Upload a CSV file containing movie data.
- Store movie data in a SQLite database.
- Query movies based on release year and languages.
- Sort movies by release date or vote average (ratings).
- Pagination support for retrieving movie lists.

## Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Pandas
- SQLite

## Setup

1. **Clone the repository**:

   ```bash 
   git clone https://github.com/your-username/movies-api.git
   cd movies-api```

2. **Create a virtual environment:**:
   ```bash python3 -m venv venv
    source venv/bin/activate```

3. **Install required packages::**:
    ```bash pip3 install -r requirements.txt```

## Running the Application

1. **Start the Flask application:**:

   ```bash flask run```
   or
   ```bash python run.py```

## API Endpoints

1. **Upload CSV File:**:
    - URL: /upload
    - Method: POST
    - Description: Upload a CSV file containing movie data and save it to the database.
    - Request Body: Multipart form-data with a file field named file.

    ```bash curl -X POST -F "file=@./movies_data_assignment.csv" http://127.0.0.1:5000/upload ```

2. **Get Movies:**:
    - URL: /movies
    - Method: GET
    - Description: Retrieve movies from the database with optional filters, sorting, and pagination.
    - Query Parameters:
    - page: (optional) Page number, defaults to 1.
    - per_page: (optional) Number of movies per page, defaults to 10.
    - release_year: (optional) Filter movies by the year of release.
    - language: (optional) Filter movies by language (in the languages column).
    - sort_by: (optional) Sort movies by either release_date or vote_average.
    - order: (optional) Sorting order, can be asc or desc, defaults to asc.

    - **Pagination**: Get the first page with 5 movies per page.
    ```bash curl -X GET "http://127.0.0.1:5000/movies?page=1&per_page=5"```

    - **Filtering by Language**: Get movies with language 'English'.
    ```bash curl curl -X GET "http://127.0.0.1:5000/movies?language=English"```

    - **Filtering by Year of Release**: Get movies released in 1995.
    ```bash curl -X GET "http://127.0.0.1:5000/movies?release_year=1995"```

    - **Sorting by Release Date**: Get movies sorted by release date in ascending order.
    ```bash curl -X GET "http://127.0.0.1:5000/movies?sort_by=release_date&order=asc"```

    - **Sorting by Ratings**: Get movies sorted by vote average (ratings) in descending order.
    ```bash curl -X GET "http://127.0.0.1:5000/movies?sort_by=vote_average&order=desc"```

    - **Combined Request**: Get the first page of movies released in 1995, filtered by language 'English', sorted by ratings in descending order.
    ```bash curl -X GET "http://127.0.0.1:5000/movies?page=10&per_page=10&release_year=1995&language=English&sort_by=vote_average&order=desc"```

3. **Delete All Movies**
    - URL: /movies
    - Method: DELETE
    - Description: Delete all entries in the movies table.

    ```bash curl -X DELETE http://127.0.0.1:5000/movies```





