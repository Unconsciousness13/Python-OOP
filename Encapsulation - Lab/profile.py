class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError(
                "The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__pasword

    @password.setter
    def password(self, value):
        if self.is_len_valid(value) and self.is_digit(value) and self.is_upper(value):
            self.__pasword = value
            return
        raise ValueError(
            f"The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def is_len_valid(self, password):
        if len(password) > 7:
            return True
        False

    def is_digit(self, password):
        nums = [num for num in password if num.isdigit()]
        return True if nums else False

    def is_upper(self, password):
        upper_letters = [char for char in password if char.isupper()]
        return True if upper_letters else False

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.__pasword)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
