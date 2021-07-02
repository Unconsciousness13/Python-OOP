from typing import List

from project.pokemon import Pokemon

class Trainer:
    name: str
    pokemon: List[Pokemon]
    def __init__(self, name: str) -> None:
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str) -> str:
        pokemon_names = [p.name for p in self.pokemon]
        if pokemon_name not in pokemon_names:  
            return 'Pokemon is not caught'

        del self.pokemon[pokemon_name.index(pokemon_name)]
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        trainer_info = [
            f'Pokemon Trainer {self.name}' ,
            f'Pokemon count {len(self.pokemon)}' ,
        ]
        pokemon_info = [f"- {p.pokemon_details()}" for p in self.pokemon]

        return '\n'.join(trainer_info + pokemon_info) + '\n'