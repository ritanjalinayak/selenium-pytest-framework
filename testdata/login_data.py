login_regression_data = [
    ("student", "Password123", "success"),
    ("student", "wrongpass", "Your password is invalid!"),
    ("wronguser", "Password123", "Your username is invalid!"),
    ("", "Password123", "Your username is invalid!"),
    ("student", "", "Your password is invalid!"),
]