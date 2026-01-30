from fastapi import FastAPI, HTTPException, Body 

app=FastAPI()

movie = [{
    "id": 1,
    "title": "Avatar",
    "overview": "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
    "year": 2009,
},{
    "id": 2,
    "title": "I Am Legend",
    "overview": "Years after a devastating virus, the sole survivor in New York City struggles to find a cure while protecting himself from nocturnal mutants.",
    "year": 2007,
},{
    "id": 3,
    "title": "300", 
    "overview": "King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.",
    "year": 2006,
}]

@app.get('/movies_all', tags=["Movie"])
def get_movies_all():
    return movie

@app.post('/movies/', tags=["Movie"])
def create_movie(
    id: int=Body(...), 
    title: str=Body(...), 
    overview: str=Body(...), 
    year: int=Body(...)):

    new_movie = {
        "id": id,
        "title": title,
        "overview": overview,
        "year": year
    }
    movie.append(new_movie)
    return new_movie

@app.get('/{id}', tags=["Movie"])
def get_root(id: int):
    for mov in movie:
        if mov["id"] == id:
            return mov
    raise HTTPException(status_code=404, detail="Movie not found")

@app.put('/{id}', tags=["Movie"])
def update_movie(
    id: int,
    title: str=Body(...), 
    overview: str=Body(...), 
    year: int=Body(...)):

    for mov in movie:
        if mov["id"] == id:
            mov["title"] = title
            mov["overview"] = overview
            mov["year"] = year
    return movie
    

@app.delete('/{id}', tags=["Movie"])
def delete_movie(id: int):      
    for mov in movie:
        if mov["id"] == id:
            movie.remove(mov)
    return movie    
    
