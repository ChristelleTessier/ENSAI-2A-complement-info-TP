from business_object.pokemon.attacker_pokemon import Attacker
from business_object.statistic import Statistic


class TestAttackerPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN  Données, ensemble des objets à construire
        attack = 100
        speed = 100
        pikachu = Attacker(stat_current=Statistic(attack=attack, speed=speed))

        # WHEN  Appel de la fonction à tester
        multiplier = pikachu.get_pokemon_attack_coef()

        # THEN  Vérifie le résultat
        assert multiplier == 2
