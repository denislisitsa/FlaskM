from flask import Flask, request, jsonify

app = Flask(__name__)


def get_listeners(city, genre):
    pass


@app.route('/stats_by_city', methods=['GET'])
def get_city_stats():
    genre = request.args.get('genre')

    if not genre:
        return jsonify(message='Жанр не указан'), 400

    cities = ["А", "Б", "с"]

    max_listeners = 0
    max_city = None

    for city in cities:
        listeners = get_listeners(city, genre)
        if listeners is not None:
            if max_city is None or listeners > max_listeners:
                max_listeners = listeners
                max_city = city

    if max_city:
        return jsonify(city=max_city)
    else:
        return jsonify(message='Жанр не найден'), 404


if __name__ == '__main__':
    app.run()
