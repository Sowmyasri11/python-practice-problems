class DuplicateUserError(Exception):
    pass


class WeakPasswordError(Exception):
    pass


class User:
    user_name = set()  # Fixed: class attribute outside __init__

    def __init__(self, username, mobile, password):
        self.username = username
        self.mobile = mobile
        self.password = password

    def addUser(self):
        if self.username in User.user_name:
            raise DuplicateUserError("User already exists")
        User.user_name.add(self.username)

    def validate(self):
        upperCase = lowerCase = specialChar = numerical = 0
        for i in self.password:
            if i.isupper():
                upperCase += 1
            elif i.islower():
                lowerCase += 1
            elif i.isdigit():
                numerical += 1
            else:
                specialChar += 1

        if (len(self.password) < 6 or upperCase == 0 or lowerCase == 0 or
                specialChar == 0 or numerical == 0):
            raise WeakPasswordError("Password is not strong enough")


def main():
    username = input("Enter the username: ")
    mobile = input("Enter the mobile number: ")
    password = input("Enter the password: ")

    try:
        user1 = User(username, mobile, password)
        user1.validate()  # Check password first
        user1.addUser()  # Then check/add username
        print("Account created successfully")
    except DuplicateUserError as e:
        print(e)
    except WeakPasswordError as e:
        print(e)
    except Exception as e:
        print("Hey, some issue occurred:", e)


main()
