# ------------  KATA DESCRIPTION ------------
"""
7 kyu - Computer problem series #2: Torrent download

Your task is to determine how much time will take to download all the files in your Torrent and the order of completion.
All downloads are started and done in parallel like in real life. In the event of a tie you should list alphabeticaly.
Help:

    GB: Giga Byte
    Mbps: Mega bits per second
    G = 1000 M
    Byte = 8 bits
    https://en.wikipedia.org/wiki/Byte
    https://en.wikipedia.org/wiki/Bandwidth_(computing)

Input:

    Array of files
    File example: {"name": "alien", "size_GB": 38.0, "speed_Mbps": 38}

Output:

    List of files in the order of completed download
    Time in seconds to download last file

Examples:

    Basic

file_1 = {"name": "alien", "size_GB": 38, "speed_Mbps": 38}
file_2 = {"name": "predator", "size_GB": 38, "speed_Mbps": 2}
file_3 = {"name": "terminator", "size_GB": 5, "speed_Mbps": 25}

torrent([file_1, file_2, file_3]) -> ["terminator", "alien", "predator"], 152000

    Order by name in case of a tie.

file_4 = {"name": "zombieland", "size_GB": 38, "speed_Mbps": 38}
file_1 = {"name": "alien", "size_GB": 38, "speed_Mbps": 38}

torrent([file_1, file_4]) -> ["alien", "zombieland"], 8000

Do not expect any invalid inputs.

"""


# ---------------  SOLUTION ---------------
def torrent(files):
    # create list (film_name, time_to_download)
    lst = [(file['name'], file["size_GB"] / file["speed_Mbps"] * 1000 * 8) for file in files]
    # sort list by time_to_download first, then by film_name
    lst = sorted(lst, key=lambda k: (k[1], k[0]))
    # return list of film_name's and time of last item of list
    return [f[0] for f in lst], lst[-1:][0][1]


# ---------------  TEST CASES ---------------
import codewars_test as test

test.describe("Computer problem series #2: uTorrent download")

file_1 = {"name": "alien", "size_GB": 38, "speed_Mbps": 38}
file_2 = {"name": "predator", "size_GB": 38, "speed_Mbps": 2}
file_3 = {"name": "terminator", "size_GB": 5, "speed_Mbps": 25}
file_4 = {"name": "zombieland", "size_GB": 38, "speed_Mbps": 38}

# Basic
test.it("Basic tests")
files = [file_1, file_2, file_3]
test.assert_equals(torrent(files), (["terminator", "alien", "predator"], 152000))

# Order by name in case of a tie
test.it("Tie tests")
files = [file_1, file_4]
test.assert_equals(torrent(files), (["alien", "zombieland"], 8000))

files = [file_4, file_1]
test.assert_equals(torrent(files), (["alien", "zombieland"], 8000))

# import random
from random import randint, sample, choice

# tie tests: high probability of same size and speed between 2 o more films
@test.it("Tie tests")
def tests():
    NAMES_TIE = ("alien", "aliens", "alien 3", "alien resurection", "alien covenant",
                 "alien prometheus", "alien vs predator", "alien vs predator 2",
                 "die hard", "die hard 2", "die hard 3", "die hard 4", "die hard 5")
    NUMERIC_TIE = (40, 80, 160)

    def torrent_solution_(files):
        time = max(file.get("size_GB") * 8000 / file.get("speed_Mbps") for file in files)
        return [file.get("name") for file in
                sorted(files, key=lambda x: (x.get("size_GB") / x.get("speed_Mbps"), x.get("name")))], time

    for _ in range(100):
        # create list of n files
        n = randint(1, len(NAMES_TIE))
        names = sample(NAMES_TIE, n)
        sizes = [choice(NUMERIC_TIE) for _ in range(n)]
        speeds = [choice(NUMERIC_TIE) for _ in range(n)]
        files = [{"name": name, "size_GB": size, "speed_Mbps": speed} for name, size, speed in
                 zip(names, sizes, speeds)]
        # test.assert_equals(torrent(files), torrent_solution_(files))
        list_files_solution, float_time_solution = torrent_solution_(
            files)  # create expected result before calculating user's solution
        list_files, float_time = torrent(files)
        test.assert_equals(list_files, list_files_solution)
        test.assert_approx_equals(float_time, float_time_solution)


# random tests: random sizes and speeds
@test.it("Random tests")
def tests2():
    NAMES = ("alien", "terminator", "predator", "lethal weapon", "die hard", "speed", "matrix", "john wick",
             "avatar", "avengers", "titanic", "dogma", "mallrats", "hellboy", "aquaman", "carrie", "apocalipsys now",
             "oscar", "cube", "solaris", "inception", "batman")

    def torrent_solution_(files):
        time = max(file.get("size_GB") * 8000 / file.get("speed_Mbps") for file in files)
        return [file.get("name") for file in
                sorted(files, key=lambda x: (x.get("size_GB") / x.get("speed_Mbps"), x.get("name")))], time

    for _ in range(100):
        # create list of n files
        n = randint(1, len(NAMES))
        names = sample(NAMES, n)
        sizes = [randint(1, 100) for _ in range(n)]
        speeds = [randint(1, 100) for _ in range(n)]
        files = [{"name": name, "size_GB": size, "speed_Mbps": speed} for name, size, speed in
                 zip(names, sizes, speeds)]

        # test.assert_equals(torrent(files), torrent_solution_(files))
        list_files_solution, float_time_solution = torrent_solution_(
            files)  # create expected result before calculating user's solution
        list_files, float_time = torrent(files)
        test.assert_equals(list_files, list_files_solution)
        test.assert_approx_equals(float_time, float_time_solution)