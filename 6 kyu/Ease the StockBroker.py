# ------------  KATA DESCRIPTION ------------
"""
6 kyu - Ease the StockBroker

Clients place orders to a stockbroker as strings. The order can be simple or multiple.

Type of a simple order: Quote/white-space/Quantity/white-space/Price/white-space/Status

where Quote is formed of non-whitespace character, Quantity is an int, Price a double (with mandatory decimal point "." ), Status is represented by the letter B (buy) or the letter S (sell).

Example:

"GOOG 300 542.0 B"

A multiple order is the concatenation of simple orders with a comma between each.

Example:

"ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG 20 580.1 B"

or (C)

"ZNGA 1300 2.66 B,CLH15.NYM 50 56.32 B,OWW 1000 11.623 B,OGG 20 580.1 B"

To ease the stockbroker your task is to produce a string of type

"Buy: b Sell: s" where b and s are 'double' formatted with no decimal, b representing the total price of bought stocks and s the total price of sold stocks.

Example:

"Buy: 294990 Sell: 0"

Unfortunately sometimes clients make mistakes. When you find mistakes in orders, you must pinpoint these badly formed orders and produce a string of type:

"Buy: b Sell: s; Badly formed nb: badly-formed 1st simple order ;badly-formed nth simple order ;"

where nb is the number of badly formed simple orders, b representing the total price of bought stocks with correct simple order and s the total price of sold stocks with correct simple order.

Examples:

"Buy: 263 Sell: 11802; Badly formed 2: CLH16.NYM 50 56 S ;OWW 1000 11 S ;"

"Buy: 100 Sell: 56041; Badly formed 1: ZNGA 1300 2.66 ;"

Notes:

    Due to Codewars whitespace differences will not always show up in test results.
    With Golang use a format with "%.0f" for "Buy" and "Sell".

"""

# ---------------  SOLUTION ---------------
import codewars_test as test


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def is_float(string):

    try:
        float(string)
        if string.find(".") == -1:
            return False
        return True
    except ValueError:
        return False


def balance_statement(lst):

    if not len(lst):
        return "Buy: 0 Sell: 0"

    tb = 0
    ts = 0
    nb = 0
    err = str()

    orders = lst.split(', ')

    for order in orders:
        o = order.split(' ')

        if len(o) == 4 and is_int(o[1]) and is_float(o[2]) and o[3] in {'B', 'S'}:
            if o[3] == 'B':
                tb += int(o[1]) * float(o[2])
            elif o[3] == 'S':
                ts += int(o[1]) * float(o[2])
        else:
            nb += 1
            err += order + " ;"

    result = "Buy: {} Sell: {}".format(str(round(tb)).split('.')[0], str(round(ts)).split('.')[0])

    if nb:
        result += "; Badly formed {}: {}".format(nb, err)

    return result


# ---------------  TEST CASES ---------------
# test.assert_equals(
#     balance_statement("ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG 20 580.1 B"),
#     "Buy: 29499 Sell: 0")

balance_statement("CAP 4948 17.97 B")

test.assert_equals(balance_statement("GOOG 300 542.93 B, CLH15.NYM 50 56.32 S, CSCO 250 29.46 B, OGG 20 580.1 B"),
                   'Buy: 181846 Sell: 2816')
