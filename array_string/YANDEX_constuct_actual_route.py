"""
Given the list of routes, we need restore order of routes. See the example below.

input:
[
    {"from": 'C', "to": 'Minsk'},
    {"from": 'Kiev', "to": 'N'},
    {"from": 'CH', "to": 'Moscow'},
    {"from": 'Minsk', "to": 'Kiev'},
    {"from": 'Moscow', "to": 'C'},
]

output:
[
    {"from": 'CH', "to": 'Moscow'},
    {"from": 'Moscow', "to": 'C'},
    {"from": 'C', "to": 'Minsk'},
    {"from": 'Minsk', "to": 'Kiev'},
    {"from": 'Kiev', "to": 'N'},
]
"""

from itertools import permutations
from typing import List

import pytest


# O(N) time | O(N) space
def restore_route(routes: List[dict]) -> List[dict]:
    def find_difference(set1: set, set2: set) -> str:
        return list(set1.difference(set2))[0]

    from_cities_dict = {route["from"]: idx for idx, route in enumerate(routes)}
    to_cities_set = {route["to"] for route in routes}

    next_city = find_difference(set(from_cities_dict.keys()), to_cities_set)

    new_routes = []  # To-do
    for i in range(len(routes)):
        starting_city_index = from_cities_dict.get(next_city)
        next_city = routes[starting_city_index]["to"]
        new_routes.append(routes[starting_city_index])

    return new_routes


# O(N) time | O(N) space, but we don't create new_routes in this solution.
def restore_route_better_solution(routes: List[dict]) -> List[dict]:
    def find_difference(set1: set, set2: set) -> str:
        return list(set1.difference(set2))[0]

    from_cities_dict = {route["from"]: idx for idx, route in enumerate(routes)}
    to_cities_set = {route["to"] for route in routes}

    next_city = find_difference(set(from_cities_dict.keys()), to_cities_set)

    for i in range(len(routes) - 1):
        starting_city_index = from_cities_dict.get(next_city)
        from_cities_dict[routes[i]["from"]] = starting_city_index  # Need to update from_cities_dict because we swap.
        next_city = routes[starting_city_index]["to"]
        routes[i], routes[starting_city_index] = routes[starting_city_index], routes[i]

    return routes


@pytest.mark.parametrize("input_data", permutations([
    {"from": 'C', "to": 'Minsk'},
    {"from": 'Minsk', "to": 'Kiev'},
    {"from": 'CH', "to": 'Moscow'},
    {"from": 'Kiev', "to": 'N'},
    {"from": 'Moscow', "to": 'C'},
]))
def test_restore_route(input_data):
    input_data = list(input_data)
    expected_result = [
        {"from": 'CH', "to": 'Moscow'},
        {"from": 'Moscow', "to": 'C'},
        {"from": 'C', "to": 'Minsk'},
        {"from": 'Minsk', "to": 'Kiev'},
        {"from": 'Kiev', "to": 'N'},
    ]
    solution1_actual_result = restore_route(input_data)
    solution2_actual_result = restore_route_better_solution(input_data)
    assert solution1_actual_result == solution2_actual_result == expected_result
