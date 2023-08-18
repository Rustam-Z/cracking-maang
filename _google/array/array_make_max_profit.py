"""
Given you are a consultant who need to travel to two cities and need to get most profit. Given two array of Integer,
CityA and CityB where CityA(i) -> is earnings of consultant on day i, see what path consultant should take to get maximum earnings.

Constraints:
    - CityA and CityB are of same length
    - Tou can start from either CityA or CityB
    - if Consultant is travelling from city A to city B -> earnings = 0

Example
CityA: [23,4,5,10}
CityB: [21,1,10,100]
answer: "ATBB", T stands for travel.
"""

from typing import List
from collections import namedtuple

ProfitPath = namedtuple('ProfitPath', ('profit', 'path'))


def find_max_profit_path(CityA: List[int], CityB: List[int]) -> str:
    a_prev, b_prev = ProfitPath(0, []), ProfitPath(0, [])
    a_curr, b_curr = ProfitPath(CityA[0], ['A']), ProfitPath(CityB[0], ['B'])

    for i in range(1, len(CityA)):
        a_next = ProfitPath(a_curr.profit + CityA[i], a_curr.path[:] + ['A'])
        a_next = max(a_next, ProfitPath(b_prev.profit + CityA[i], b_prev.path[:] + ['TA']))

        b_next = ProfitPath(b_curr.profit + CityB[i], b_curr.path[:] + ['B'])
        b_next = max(b_next, ProfitPath(a_prev.profit + CityB[i], a_prev.path[:] + ['TB']))

        a_prev, a_curr = a_curr, a_next
        b_prev, b_curr = b_curr, b_next

    return ''.join(max(a_curr, b_curr)[1])


if __name__ == '__main__':
    CityA = [23, 4, 5, 10]
    CityB = [21, 1, 10, 100]
    assert find_max_profit_path(CityA, CityB) == 'ATBB'

    CityA = [50]
    CityB = [10]
    assert find_max_profit_path(CityA, CityB) == 'A'

    CityA = [10, 10]
    CityB = [10, 10]
    assert find_max_profit_path(CityA, CityB) == 'BB'  # or AA

    CityA = [90, 10]
    CityB = [10, 99]
    assert find_max_profit_path(CityA, CityB) == 'BB'

    CityA = [90, 10, 99, 10]
    CityB = [10, 1, 99, 99]
    assert find_max_profit_path(CityA, CityB) == 'ATBB'

    CityA = [90, 10, 99, 200]
    CityB = [10, 1, 99, 99]
    assert find_max_profit_path(CityA, CityB) == 'AAAA'

    CityA = [10, 5, 4, 6]
    CityB = [9, 3, 7, 11]
    assert find_max_profit_path(CityA, CityB) == 'BBBB'
