# number of movies released in 2022

# f=open("movies.txt","r")
# movies_list=[]
# for m in f:
#     movie=m.rstrip("\n").split(",")
#     movies_list.append(movie)
# print(movies_list)

#              OR

# movie=[m.rstrip("\n").split(",") for m in f]
# # print(movie)
#
# two_two=[t for t in movie if t[1]=="2022"]
# print(len(two_two))


# number malayalam movies

# f=open("movies.txt","r")
# movies_list=[m.rstrip("\n").split(",") for m in f]
# # print(movies_list)
# mal_movies=[m for m in movies_list if m[3]=="malayalam"]
# # print(mal_movies)
# print(len(mal_movies))


# theater released movies

# f=open("movies.txt","r")
# movies_list=[m.rstrip("\n").split(",") for m in f]
# theatre_release=[m for m in movies_list if m[4]=="theatre"]
# print(len(theatre_release))

# list of movies whose rating > 5

# f=open("movies.txt","r")
# movies_list=[m.rstrip("\n").split(",") for m in f]
# ratings=[m for m in movies_list if m[2]>"5"]
# print(ratings)


# {2022:,4,2021:6,2020:2}

# same as word_count program


movies_out = {}
f = open("movies.txt", "r")
movies_list = [m.rstrip("\n").split(",") for m in f]
for m in movies_list:
    year = m[1]
    if year in movies_out:
        movies_out[year] += 1
    else:
        movies_out[year] = 1

print(movies_out)

# sort in descending

print(sorted(movies_out.values(), reverse=True))

# print most number of movies released in the dict

print(max(movies_out.items(), key=lambda ite: ite[1]))
