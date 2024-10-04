from flask import request, jsonify
from . import db
from .models import Movie
import pandas as pd
import os
from datetime import datetime

def register_routes(app):
    @app.route('/upload', methods=['POST'])
    def upload_csv():
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        
        file = request.files['file']
        file_path = os.path.join('/tmp', file.filename)
        file.save(file_path)
        
        try:
            df = pd.read_csv(file_path)

            for _, row in df.iterrows():
                release_date = row['release_date']
                if isinstance(release_date, str): 
                    release_date = datetime.strptime(release_date, '%Y-%m-%d')
                elif pd.isna(release_date): 
                    release_date = None

                movie = Movie(
                    title=row['title'],
                    budget=row['budget'],
                    homepage=row['homepage'],
                    original_language=row['original_language'],
                    overview=row['overview'],
                    release_date=release_date,
                    revenue=row['revenue'],
                    runtime=row['runtime'],
                    status=row['status'],
                    vote_average=row['vote_average'],
                    vote_count=row['vote_count'],
                    production_company_id=row['production_company_id'],
                    genre_id=row['genre_id'],
                    languages=str(row['languages']).strip("[]'")
                )
                db.session.add(movie)
            db.session.commit()
            return jsonify({"message": "CSV uploaded successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/movies', methods=['GET'])
    def get_movies():
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        release_year = request.args.get('release_year')
        language = request.args.get('language')
        sort_by = request.args.get('sort_by', 'release_date') 
        order = request.args.get('order', 'asc') 

        query = Movie.query
        if release_year:
            query = query.filter(Movie.release_date.like(f"{release_year}%"))
        if language:
            query = query.filter(Movie.languages.like(f"%{language}%"))

        if sort_by == 'release_date':
            if order == 'desc':
                query = query.order_by(Movie.release_date.desc())
            else:
                query = query.order_by(Movie.release_date.asc())
        elif sort_by == 'ratings':
            if order == 'desc':
                query = query.order_by(Movie.vote_average.desc())
            else:
                query = query.order_by(Movie.vote_average.asc())

        movies = query.paginate(page=page, per_page=per_page, error_out=False)

        results = [{"title": movie.title, "release_date": movie.release_date, "languages": movie.languages,
                    "overview": movie.overview, "budget": movie.budget, "revenue": movie.revenue, "runtime": movie.runtime,
                    "status": movie.status, "vote_average": movie.vote_average, "vote_count": movie.vote_count,
                    "production_company_id": movie.production_company_id, "genre_id": movie.genre_id} 
                for movie in movies.items]
        
        return jsonify({
            "movies": results,
            "total": movies.total,
            "page": movies.page,
            "per_page": movies.per_page
        })

    @app.route('/movies', methods=['DELETE'])
    def delete_all_movies():
        try:
            db.session.query(Movie).delete()  
            db.session.commit()
            return jsonify({"message": "All movies deleted successfully."}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

