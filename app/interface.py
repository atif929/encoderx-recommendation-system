import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

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

data = pd.merge(ratings, movies, on="movie_id")

movie_user = data.pivot_table(
    index="title",
    columns="user_id",
    values="rating"
).fillna(0)

movie_similarity = pd.DataFrame(
    cosine_similarity(movie_user),
    index=movie_user.index,
    columns=movie_user.index
)

print("=" * 50)
print("Movie Recommendation System")
print("=" * 50)

movie_name = input("\nEnter a movie name: ").strip()

matches = [
    title for title in movie_similarity.index
    if movie_name.lower() in title.lower()
]

if len(matches) == 0:
    print("\nMovie not found.")
    exit()

if len(matches) > 1:

    print("\nMultiple movies found:\n")

    for i, title in enumerate(matches, start=1):
        print(f"{i}. {title}")

    choice = int(input("\nSelect a movie number: "))

    movie = matches[choice - 1]

else:

    movie = matches[0]

print("\nMovie Selected")
print("-------------------")
print(movie)

average = data[data["title"] == movie]["rating"].mean()

total = data[data["title"] == movie]["rating"].count()

print(f"\nAverage Rating : {average:.2f}")

print(f"Total Ratings  : {total}")

print("\nTop 10 Recommended Movies")
print("---------------------------")

recommendations = movie_similarity[movie].sort_values(
    ascending=False
)[1:11]

for i, title in enumerate(recommendations.index, start=1):
    print(f"{i}. {title}")