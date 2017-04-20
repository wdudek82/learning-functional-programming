# https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming

from random import random, choice
from operator import add


sentences = ['Mary read a story to Sam and Isla.',
             'Isla cuddled Sam.',
             'Sam chortled.']

# print(reduce(lambda a, x: a + x.count("Sam"), sentences, 0))

names = ["Wojtek", "Kuba", "Jurek"]
codenames = ["orange", "green", "black"]
# print(map(lambda x: choice(codenames), names))
# print(map(lambda x: hash(x), names))

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

heights = map(lambda x: x["height"], filter(lambda x: "height" in x, people))
height_average = reduce(add, heights) / len(heights)
print(height_average)


# functional car race
car_positions = [1, 1, 1]


def move_cars(car_positions):
    return map(lambda x: x + 1 if random() > 0.4 else x, car_positions)


def output_car(car_position):
    return "-" * car_position


def run_step_of_race(state):
    return {"time": state["time"] - 1,
            "car_positions": move_cars(state["car_positions"])}


def draw(state):
    print ""
    print "\n".join(map(output_car, state["car_positions"]))


def race(state):
    draw(state)
    if state["time"]:
        race(run_step_of_race(state))


race({"time": 5,
      "car_positions": [1, 1, 1]})


# functional rule sequencer
def zero(s):
    if s[0] == "0":
        return s[1:]


def one(s):
    if s[0] == "1":
        return s[1:]


rules1 = [zero, one, zero]
rules2 = [zero, zero, one]

s = "0101"


def rule_sequence(s, rules):
    if s and rules:
        print(s, rules)
        return rule_sequence(rules[0](s), rules[1:])
    else:
        return s

# print(rule_sequence(s, rules2))

# functional/recusive loop
def recursive_loop(start, stop, step=1):
    if start < stop:
        print("Looping: %d" % start)
        recursive_loop(start + step, stop, step)

# recursive_loop(5, 20)
recursive_loop(5, 25, 2)
# recursive_loop(5, 35, 5)

# recursion with random base case
def rand_base_recursion(base=0):
    rand_num = random.randint(0, base+10)
    print("Looping: %d" % rand_num)
    if base != rand_num:
        rand_base_recursion(base)
