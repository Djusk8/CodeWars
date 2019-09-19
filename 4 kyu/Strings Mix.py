import codewars_test as Test


def mix(s1, s2):

    common_set = [char for char in sorted(set(s1 + s2)) if char.islower()]  # all chars occurred in both strings

    mas = []

    for char in common_set:

        l1, l2 = s1.count(char), s2.count(char)  # counts number of "chars" in s1 and s2 strings

        if l1 > 1 or l2 > 1:

            if l1 == l2:
                mas.append((l1, "=:" + str(char) * l1))

            elif l1 != l2:
                mas.append((max(l1, l2), ("1" if l1 > l2 else "2") + ":" + str(char) * max(l1, l2)))

    mas.sort(key=lambda row: row[1])
    mas.sort(key=lambda row: row[0], reverse=True)

    return '/'.join([item[1] for item in mas])


Test.describe("Mix")
Test.it("Basic Tests")
Test.assert_equals(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
Test.assert_equals(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
Test.assert_equals(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
Test.assert_equals(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
Test.assert_equals(mix("codewars", "codewars"), "")
Test.assert_equals(mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")