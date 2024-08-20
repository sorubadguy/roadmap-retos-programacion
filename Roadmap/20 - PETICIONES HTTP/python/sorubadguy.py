import requests

#? Peticiones HTTP

class peticiones():
    
    def __init__(self, link: str) -> None:
        self.link = requests.get(link)
        if(self.link.ok):
            print(self.link.text)
        else:
            print(f"Error {self.link}")
    

w3schools = peticiones("https://w3schools.com/python/demopage.htm")
w3schools2 = peticiones("https://www.w3schools.com/python/dfsfeerqerq")

#! Extra

def pokemons(nombre: str):
    pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nombre}").json()
    print(f"ID: {pokemon['id']}\nNombre: {pokemon['name']}\nTipo/s:")
    for tipo in pokemon['types']:
        print(f"\ttipo{tipo['slot']}: {tipo['type']['name']}")
    print(f"Altura: {pokemon['height']/10} mts\nPeso: {pokemon['weight']/10} Kgs")
    evoluciones = requests.get(f"https://pokeapi.co/api/v2/evolution-chain/{pokemon['id']}").json()
    cadena_evoluciones = requests.get(evoluciones['chain']['species']['url']).json()
    print(cadena_evoluciones)


pokemons("rattata")