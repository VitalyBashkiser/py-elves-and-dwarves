from typing import List, Union
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.player import Player


def calculate_team_total_rating(players: List[Player]) -> int:
    total_rating = 0
    for player in players:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: List[Union[ElfRanger, Druid]]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Union[DwarfWarrior, DwarfBlacksmith]]) \
        -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
