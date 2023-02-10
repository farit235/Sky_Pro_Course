# файл для создания DAO и сервисов чтобы импортировать их везде
from HW_18.dao.director import DirectorDAO
from HW_18.dao.genre import GenreDAO
from HW_18.dao.movie import MovieDAO
from HW_18.service.director import DirectorService
from HW_18.service.genre import GenreService
from HW_18.service.movie import MovieService
from HW_18.setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(dao=genre_dao)