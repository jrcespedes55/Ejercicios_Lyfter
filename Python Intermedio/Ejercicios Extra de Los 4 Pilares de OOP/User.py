from abc import ABC, abstractmethod

class User(ABC):

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass

class AdminUser(User):

    def __init__(self, name):
        self.name = name
        self.role = "Admin"

    def get_role(self):
        return self.role

    def has_permission(self, permission):
        return True


class RegularUser(User):

    def __init__(self, name):
        self.name = name
        self.role = "Regular"

    def get_role(self):
        return self.role

    def has_permission(self, permission):
        if permission == "read" or permission == "Read":
            return True
        else:
            return False

def main():

    user1 = AdminUser("Carlos")
    user2 = RegularUser("Andrea")

    print(f"El rol de {user1.name}: {user1.get_role()}")  
    print(f"El rol de {user2.name}: {user2.get_role()}")  

    print(user1.has_permission("delete"))  
    print(user2.has_permission("delete"))  


if __name__ == "__main__":
    main()