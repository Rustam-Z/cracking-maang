"""1169. Invalid Transactions
https://leetcode.com/problems/invalid-transactions/

Problem:
    Detect invalid transactions.
    A transaction is possibly invalid if the amount exceeds $1000, or,
    if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

Input: list[str], str represents the transaction, representing the name, time, amount, and city of the transaction.
    For example. transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: list of invalid transactions

Solution:
    - Use the dictionary, keys are people names, values are the indexes in transactions list (input).
    - And use the set, to save the bad transaction indexes.
    - And in the end, fetch that transactions from transactions list and return.
    - Main logic:
        - If the person sends money for the first time, we check if the amount is more than 1000.
        - If the person send the money before. We check the time and cities with all other previous cities.
        - Don't forget to add the transaction to dict in both cases.
"""
from typing import List


def invalidTransactions(transactions: List[str]) -> List[str]:
    result = set()  # Because we want O(1) access time, we will save transactions indexes
    trans_grouped_by_name = {}  # {name: [indexes of transactions]}

    for idx, trans in enumerate(transactions):
        name, time, amount, city = trans.split(",")

        if name not in trans_grouped_by_name:
            trans_grouped_by_name[name] = [idx]
            if int(amount) > 1000:
                result.add(idx)
        else:  # What if the person already made the transaction?
            prev_trans = trans_grouped_by_name[name]

            for idx2 in range(len(prev_trans)):
                prev_name, prev_time, prev_amount, prev_city = transactions[prev_trans[idx2]].split(",")
                if int(amount) > 1000:
                    result.add(idx)

                if abs(int(time) - int(prev_time)) <= 60 and city != prev_city:
                    result.add(idx)
                    result.add(prev_trans[idx2])

            trans_grouped_by_name[name].append(idx)

    return [transactions[i] for i in result]
