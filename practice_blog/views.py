from practice_blog.models import users




# authenticate

session={}
# us_er=[user for user in users if user["username"]==username and user["password"]==password ]
# print(us_er)

def authenticate(*args, **kwargs):
    username = kwargs.get("username")
    password = kwargs.get("password")
    us_er = [user for user in users if user["username"] == username and user["password"] == password]
    return us_er


# print(authenticate(username="akhil", password="Password@123"))

# print(authenticate(username="vinu",password="Password@123"))

class LoginView:
    def post(self, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        usr = authenticate(username=username, password=password)
        print(usr)


loginview = LoginView()
loginview.post(username="jhon", password="Password@123")

# =================================================================


from Blog.models import users, posts

# print(users)

# username="akhil"
# password="Password@123"

# authentication


# get
# post
# put/patch
# delete

session = {}


def signin_required(fn):
    def wrapper(*args, **kwargs):
        if "user" in session:
            return fn(*args, **kwargs)
        else:
            print("invalid session u must login")

    return wrapper


def authenticate(**kwargs):
    username = kwargs.get("username")
    password = kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user


# print(authenticate(username="akhil",password="Password@123"))

class LoginView:

    def post(self, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        user = authenticate(username=username, password=password)
        if user:
            session["user"] = user[0]

        print(session)


class PostListView:
    @signin_required
    def get(self, *args, **kwargs):
        return posts
    @signin_required
    def post(self,*args,**kwargs):
        print(kwargs)
        my_post=kwargs


class MyPostListView:

    @signin_required
    def get(self, *args, **kwargs):
        return posts


class AddLike:
    @signin_required
    def post(self,*args,**kwargs):
        postid=kwargs.get("postid")
        post=[post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["Liked_by"].append(userid)
            print(post["Liked_by"])



log_in = LoginView()
log_in.post(username="akhil", password="Password@123")
all_post = PostListView()
print(all_post.get())
myposts = MyPostListView()
print(myposts.get())
like=AddLike()
like.post(postid=1)