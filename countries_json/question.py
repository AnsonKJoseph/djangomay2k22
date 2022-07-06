# import json
# with open("countries.json",encoding="utf-8") as f:
#     data=json.load(f)
# # print(data)

#
# india_detail=[country for country in data if country["name"]=="India"]
# print(india_detail)

# print total number of country details

# import json
# with open("countries.json",encoding="utf-8") as f:
#     data=json.load(f)
# print(len(data))

# print languages of ukraine

import json

with open("countries.json", encoding="utf-8") as f:
    data = json.load(f)

# india_detail=[country for country in data if country["name"]=="India"]
# print(india_detail)

# language_by_country=[country["languages"] for country in data if country["name"]=="Ukraine"]
# print(language_by_country)
# for lan in language_by_country[0]:
#     print(lan["name"])

# print currency of china
#
# currency_by_country = [country["currencies"] for country in data if country["name"] == "Palestine"]
# # print(currency_by_country)
# for c in currency_by_country[0]:
#     print(c["name"])



# print currency of Palestine

# currency_by_country=[currency["currencies"] for currency in data if currency["name"].lower().startswith("palestine")]     # startswith
# print(currency_by_country)
# currency_name=[details.get("name") for details in currency_by_country[0]]
# print(currency_name)




# print population of india


# population_by_country = [population["population"] for population in data if population["name"] == "India"]
# print(population_by_country)

# print neighbouring countries of australia

# neighbouring_countries=[neighbour.get("borders")for neighbour in data if neighbour["name"]=="India"]
# print(neighbouring_countries)


#      OR

# we can do it in a function

def get_country_data(country_name):
    return [country for country in data if country["name"].lower().startswith(country_name)]
country_data=get_country_data("austria")
print(country_data[0].get("borders"))



# print names of countries which share borders with india (not code names)

country_data=get_country_data("india")
country_borders=country_data[0].get("borders")
sharing_borders=[country.get("name") for country in data if country["alpha3Code"] in country_borders]
print(sharing_borders)

# print country having the highest population

populated_country=(max(data,key=lambda d:d.get("population")))
print(populated_country["name"])

# print country having the lowest population

low_population=(min(data,key=lambda d:d.get("population")))
print(low_population["name"])