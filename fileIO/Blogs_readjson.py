import json

with open("blogs.json",encoding="utf-8") as f:               # this is common for all json programs
    data=json.load(f)
    # print(data)

print(len(data))

# number of post by userId=1

my_post_by_user=[post for post in data if post["userId"]==1]
print(len(my_post_by_user))

# total number of likes for postId 6

num_likes_post=[len(post["liked_by"]) for post in data if post["postId"]==6]
print(num_likes_post)

# number of posts liked by user =2

like_count_user=len([post for post in data if 2 in post["liked_by"]])
print(like_count_user)

like=[ like["liked_by"] for like in data if like["title"]=="hello"]
print(like)