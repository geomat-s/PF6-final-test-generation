import requests
import json

def main():
  user_number = input("Hola, digita un número y te daré información sobre un plato típico de mi país, Colombia: ")
   
  info_dish = dish_fetch(user_number)
  #print(info_dish)
  print(f"El número: {user_number} es el plato llamado: {info_dish["name"]}. \n{info_dish["description"]} Finalmente sus ingredientes son: {info_dish["ingredients"]}")

def dish_fetch(num):

  response = requests.get(f"https://api-colombia.com/api/v1/TypicalDish/{num}")
  responseJson = response.json()
  return responseJson

if __name__=="__main__":
  main()