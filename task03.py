class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active

u = User("diyor", "diyor@gmail.com", True)
print(u.username, u.is_active)
