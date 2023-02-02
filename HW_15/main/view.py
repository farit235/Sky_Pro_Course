from flask import Blueprint
import sqlite3

main_blueprint = Blueprint("main_blueprint", __name__)


def print_item(item_id):
    """Функция возврата значения по id"""
    query = f"""
            SELECT *
            FROM animals
            WHERE animals."index" = {item_id}
            """
    with sqlite3.connect('./animal.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result_item = []
        for row in cursor.fetchall():
            item = {"id": row[0], "outcome_age": row[1], "animal_id": row[2], "animal_type": row[3], "name": row[4],
                    "breed": row[5], "color_1": row[6],  "color_2": row[7], "date": row[8], "outcome_subtype": row[9],
                    "outcome_type": row[10], "outcome_month": row[11], "outcome_year": row[12]}
            result_item.append(item)
    return result_item


@main_blueprint.route("/<int:item_id>")
def search_func(item_id):
    return print_item(item_id)


#  изменение таблицы
query_1 = """
              CREATE TABLE IF NOT EXISTS colors
                (
                 color_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 color varchar(100) 
                )
          """

query_2 = """
            CREATE TABLE IF NOT EXISTS breeds
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                breed VARCHAR(100)
            )
          """

query_3 = """
            INSERT INTO breeds (breed)
            SELECT DISTINCT animals.breed AS breed FROM animals
          """

query_4 = """  
              CREATE TABLE IF NOT EXISTS animals_colors
                (
                    animal_id INTEGER,
                    color_id INTEGER,
                    FOREIGN KEY (animal_id) REFERENCES animals_final(id),
                    FOREIGN KEY (color_id) REFERENCES colors(id)
                )
          """

query_5 = """
            INSERT INTO colors (color)
                SELECT DISTINCT * FROM
                (SELECT DISTINCT animals.color1 AS color FROM animals
                UNION ALL
                SELECT DISTINCT animals.color2 AS color FROM animals)
          """

query_6 = """
            INSERT INTO animals_colors (animal_id, color_id)
            SELECT DISTINCT animals_final.id, colors.color_id FROM animals
            JOIN colors ON colors.color = animals.color1
            JOIN animals_final ON animals_final.animal_id = animals.animal_id  
            UNION ALL 
            SELECT DISTINCT animals_final.id, colors.color_id FROM animals
            JOIN colors ON colors.color = animals.color2
            JOIN animals_final ON animals_final.animal_id = animals.animal_id 
          """

query_7 = """
            CREATE TABLE IF NOT EXISTS outcome
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    subtype VARCHAR(50),
                    "type" VARCHAR(50),
                    "month" INTEGER,
                    "year" INTEGER
                )
          """

query_8 = """
            INSERT INTO outcome (subtype, "type", "month", "year")
            SELECT animals.outcome_subtype, animals.outcome_type , animals.outcome_month , animals.outcome_year FROM animals
          """

query_9 = """
            CREATE TABLE IF NOT EXISTS animals_final
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                age_upon_outcome VARCHAR(50),
                animal_id VARCHAR(50),
                animal_type VARCHAR(50),
                name VARCHAR(50),
                breed_id INTEGER,
                date_of_birth VARCHAR(50),
                outcome_id INTEGER,
                FOREIGN KEY (outcome_id) REFERENCES outcome(id),
                FOREIGN KEY (breed_id) REFERENCES breeds(id)
            )
          """

query_10 = """
            INSERT INTO animals_final (age_upon_outcome, animal_id, animal_type, name, date_of_birth, outcome_id, breed_id)
            SELECT animals.age_upon_outcome, animals.animal_id , animals.animal_type , animals.name, animals.date_of_birth, outcome.id, breeds.breed  FROM animals 
            JOIN outcome ON outcome.subtype = animals.outcome_subtype 
                         AND outcome."type" = animals.outcome_type 
                         AND outcome."month" = animals.outcome_month  
                         AND outcome."year" = animals.outcome_year  
            JOIN breeds ON breeds.breed =animals.breed 
          """

query_11 = """
            SELECT animals_final.name, animals_final.breed, colors.color, outcome.*  FROM animals_final
            JOIN animals_colors ON animals_colors.animal_id = animals_final.id  
            JOIN colors ON colors.color_id  = animals_colors.color_id
            JOIN outcome ON outcome.id = animals_final.outcome_id `
          """


