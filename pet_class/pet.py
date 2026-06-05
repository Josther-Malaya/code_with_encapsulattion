class Pet:
    def __init__(self, name,age,gender,animal_type):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__animal_type = animal_type

    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age

    def set_gender(self,gender):
        self.__gender = gender

    def set_animal_type(self,animal_type):
        self.__animal_type = animal_type

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_animal_type(self):
        return self.__animal_type


