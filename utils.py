import requests
import os

USER_AGENT = "adventofcode_working_directories_creator"
YEAR = 2021


# Input file things

def load_input_file(fname):
    with open('inputs/' + fname, 'r') as f:
        return [l.strip() for l in f.readlines()]


def load_as_ints(fname):
    return [int(x) for x in load_input_file(fname)]


def download_input(day):
    user_session_id = os.environ.get('AOC_USER_SESSION_ID')
    link = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    with requests.get(url=link, cookies={"session": user_session_id}, headers={"User-Agent": USER_AGENT}) as response:
        if response.ok:
            data = response.text
            if not os.path.exists("inputs"):
                os.mkdir("inputs")
            input = open(f"inputs/day{day}.input", "w+")
            input.write(data.rstrip("\n"))
            input.close()
            return f"day{day}.input"
        else:
            print("Server response for input is not valid.")


# Solving things
def transpose(l):
    return list(map(list, zip(*l)))


FOUR_DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

EIGHT_DIRECTIONS = FOUR_DIRECTIONS + [
    (1, 1),
    (-1, 1),
    (-1, -1),
    (1, -1)
]

CARDINAL_DIRECTIONS = {
    'N': FOUR_DIRECTIONS[0],
    'S': FOUR_DIRECTIONS[2],
    'E': FOUR_DIRECTIONS[1],
    'W': FOUR_DIRECTIONS[3]
}

def grid(x, y, default=None):
    return [[default for _ in range(x)] for _ in range(y)]
