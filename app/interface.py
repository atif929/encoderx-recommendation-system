import joblib
import pandas as pd

model = joblib.load("../models/recommendation_model.pkl")

ratings = pd.read_csv(
    "../dataset/ml-100k/u.data",
    sep="\t",
    names=["user_id", "movie_id", "rating", "timestamp"]
)

movies = pd.read_csv(
    "../dataset/ml-100k/u.item",
    sep="|",
    encoding="latin-1",
    header=None,
    usecols=[0, 1],
    names=["movie_id", "title"]
)

print("=" * 50)
print("Movie Recommendation System")
print("=" * 50)

user_id = int(input("Enter User ID (1-943): "))

recommendations = []

for movie in movies["movie_id"]:

    prediction = model.predict(user_id, movie)

    recommendations.append(
        (movie, prediction.est)
    )

recommendations = sorted(
    recommendations,
    key=lambda x: x[1],
    reverse=True
)

print("\nTop 10 Movie Recommendations\n")

count = 0

for movie_id, score in recommendations:

    title = movies.loc[
        movies["movie_id"] == movie_id,
        "title"
    ].values[0]

    print(f"{count+1}. {title}  ({score:.2f})")

    count += 1

    if count == 10:
        break