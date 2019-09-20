import codewars_test as Test


def xo(s):
    return True if s.lower().count('o') == s.lower().count('x') else False


Test.expect(xo('xo'), 'True expected')
Test.expect(xo('xo0'), 'True expected')
Test.expect(not xo('xxxoo'), 'False expected')
