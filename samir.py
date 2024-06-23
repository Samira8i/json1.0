import json

world = {'Россия': 'Москва', 'Германия': 'Берлин', 'Китай': 'Пекин', 'США': 'Вашингтон', 'Египет': 'Каир'}


class WorkJSON:
    def __init__(self, filename):
        self.filename = filename

    def write_data(self,new):
        with open(self.filename, 'w') as f:
            json.dump(new, f)

    def load_data(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def add_country(self, country, city):
        slovar = self.load_data()
        slovar[country] = city
        return self.write_data(slovar)

    def del_country(self, country):
        slovar = self.load_data()
        if country in slovar:
            del slovar[country]
            return self.write_data(slovar)

    def find_city_by_key(self, country):
        slovar = self.load_data()
        if country in slovar:
            return slovar[country]
        else:
            return None

    def find_city_by_value(self, city):
        slovar = self.load_data()
        for key in slovar:
            if slovar[key] == city:
                return key
        return None


smt = WorkJSON("new.json")
smt.write_data(world)
print(smt.load_data())
smt.add_country("Италия", "Рим")
print(smt.load_data())
smt.del_country("США")
print(smt.load_data())
print(smt.find_city_by_key("Россия"))
print(smt.find_city_by_value("Каир"))
