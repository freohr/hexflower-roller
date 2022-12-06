
from hexflower.direction import Direction
from hexflower.navigator import Navigator
from hexflower.hexagon import Hexagon
from typing import Dict


class Flower:
    def __init__(self, nav: Navigator, hex_list: Dict[int, Hexagon], desc: str):
        self.navigator = nav
        self.hex_list = hex_list
        self.description = desc
        pass

    def get_starting_hex(self):
        return self.hex_list[self.navigator.start]

    def navigate(self, current_hex: Hexagon):
        next_direction = self.navigator.next_direction()
        return self.hex_list[current_hex.get_neighbour(next_direction)]


def parse_navigator(dct: dict):
    json_formula = dct["formula"]
    json_start = dct["start"]
    json_navigation = dct["navigation"]
    navigation = {}
    for (k, v) in json_navigation.items():
        navigation[int(k)] = Direction[v]

    navigator = Navigator(json_formula, int(json_start), navigation)
    return navigator


def parse_hexagon(dct: dict):
    json_id = dct["id"]
    json_content = dct["content"]

    json_neighbours = dct["neighbours"]
    neighbours = {}
    for (k, v) in json_neighbours.items():
        neighbours[Direction[k]] = int(v)

    hexagon = Hexagon(int(json_id), json_content, neighbours)

    return hexagon


def parse_hex_list(lst: list):
    hex_list = [parse_hexagon(hexa) for hexa in lst]
    hex_dict = {}
    for hexa in hex_list:
        hex_dict[hexa.id] = hexa

    return hex_dict


def parse_config(dct: dict, verbose: bool = False):
    parsed_navigator = parse_navigator(dct["navigator"])
    parsed_hexes = parse_hex_list(dct["hex-list"])

    extra_desc = ""
    if verbose:
        extra_desc = f'{dct["comment"]["description"]}\n{dct["comment"]["additional_info"]}'
    else:
        extra_desc = f'{dct["comment"]["description"]}'
    description = f'{extra_desc}\n\nSource: {dct["comment"]["source"]}'
    hex_flower = Flower(parsed_navigator, parsed_hexes, description)

    return hex_flower
