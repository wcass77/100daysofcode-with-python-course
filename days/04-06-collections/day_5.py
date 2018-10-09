import csv
from collections import defaultdict, namedtuple, Counter
from urllib.request import urlretrieve

# download data
movie_data = "https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv"
movies_csv = "movies.csv"
urlretrieve(movie_data, movies_csv)
Movie = namedtuple("Movie", "title year score")


def get_movies_by_director(data=movies_csv):
    directors = defaultdict(list)
    with open(data, encoding="utf-8") as f:
        for line in csv.DictReader(f):
            try:
                directors[line["director_name"]].append(
                    Movie(
                        title=line["movie_title"].replace("\xa0", ""),
                        year=int(line["title_year"]),
                        score=float(line["imdb_score"]),
                    )
                )
            except ValueError:
                continue
    return directors


def _calc_mean(movie_list):
    sum_ = 0
    movie_count = 0
    for movie in movie_list:
        if movie.year >= 1960:
            sum_ += movie.score
            movie_count += 1
    return round(sum_ / movie_count, 1)


def get_average_scores(directors):
    directors_mean = []
    for name, movies in directors.items():
        if len(movies) > 3:
            directors_mean.append((name, _calc_mean(movies)))
    directors_mean = sorted(directors_mean, key=lambda x: float(x[1]), reverse=True)
    top_directors = {}
    for i in range(20):
        name = directors_mean[i][0]
        rating = directors_mean[i][1]
        top_directors[(name, rating)] = directors[name]
    return top_directors


def print_results(directors):
    """Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output"""
    for counter, (director, score) in enumerate(directors):
        print(f"{counter+1}. {director:<52} {score}")
        print("-" * 60)
        for movie in directors[(director, score)]:
            print(f"{movie.year}] {movie.title:<50} {movie.score}")


def print_most_movies(directors):
    movie_number = Counter()
    for director, movies in directors.items():
        director = director[0]
        movie_number[director] += len(movies)
    print(movie_number.most_common(5))


def main():
    """This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py"""
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)
    print_most_movies(directors)


# Tests
def test():
    directors = get_movies_by_director()

    assert "Sergio Leone" in directors
    assert "Andrew Stanton" in directors  # has 3 movies, but not yet filtered
    assert len(directors["Sergio Leone"]) == 4
    assert len(directors["Peter Jackson"]) == 12

    movies_sergio = directors["Sergio Leone"]
    movies_nolan = directors["Christopher Nolan"]
    assert _calc_mean(movies_sergio) == 8.5
    assert _calc_mean(movies_nolan) == 8.4

    directors = get_average_scores(directors)
    assert "Andrew Stanton" not in directors  # director 3 movies now filtered out

    expected_directors = [
        "Sergio Leone",
        "Christopher Nolan",
        "Quentin Tarantino",
        "Hayao Miyazaki",
        "Frank Darabont",
        "Stanley Kubrick",
    ]
    expected_avg_scores = [8.5, 8.4, 8.2, 8.2, 8.0, 8.0]
    expected_num_movies = [4, 8, 8, 4, 4, 7]
    report = sorted(directors.items(), key=lambda x: float(x[0][1]), reverse=True)
    for counter, (i, j, k) in enumerate(
        zip(expected_directors, expected_avg_scores, expected_num_movies)
    ):
        assert report[counter][0] == (i, j)
        assert len(report[counter][1]) == k
        assert _calc_mean(report[counter][1]) == j

    return "tests pass"


if __name__ == "__main__":
    main()
    print(test())
