import os
import sys
import math

# https://topaz.github.io/paste/#XQAAAQA1AwAAAAAAAAA0m0pnuFI8c+fPp4GmTLx+DjkmnwLhmkXe8B8w/NStqQQu2EwRmz1DReGmjZSKmlkJLilGFwYGH2B8fc+oSa1QrhLKG8q1jGqrlxM6n91XhO1X/q9mgYXbsyq+y1jiH1eG68oHOV9/7XR/mfciZHIuzawC5rr/YqOBuAgQSvdXBZqsv1sBJot5SWVZd7o+Gq7KrdQq8YQbFhV+AM2OW4AqtpXn3WINkkgtbqf/+RKTDvcs+kFi6bZeJTXWuIsdovvFIjDY3pQv3alsLwOqdTTeZxtmS9tekPRSMoFAnQDT0yH+egVh0CDNMeNS628LVf0oHq3E5JezYVrfsb7n7bBT11qzSk4jSwqy3xCSFC0a+uqJSYNt+8SeGecWrhyNCbXMBHu/FFSOPWIznScmA/gF7bbcTR3w5++Jey1k1Ot3BKYHZKoiKlFUV+zMjZ7VIgIhG2J7q6IVzvjTrPms2T+Au3PluVqSgpgkvQ5V/tgctnzr6DQY12zBBos6ILJhXhpuvDrZ9y24wP4nXLuzjAmgqoTMbTczdOKOCtDY//fYLIU=
# newline at the end of input, change when my own


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        data = f.read().splitlines()

        # PART 1
        directions = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
        steps = get_steps(data, part=1)
        part1 = get_area(steps, directions)

        # PART 2
        directions = {"0": (0, 1), "1": (1, 0), "2": (0, -1), "3": (-1, 0)}
        steps = get_steps(data, part=2)
        part2 = get_area(steps, directions)

        print(part1, part2)


def get_steps(data, part):
    steps = []
    for line in data:
        direction, length, _ = line.split()
        if part == 1:
            length = int(length)
        else:
            direction = line.split()[-1][-2]
            length = line.split()[-1][-7:-2]
            length = int(length, 16)

        steps.append((direction, length))

    return steps


def get_area(steps, directions):
    x = 0
    y = 0
    perimeter = 0
    area = 0
    for step in steps:
        direction, length = step
        dy, dx = directions[direction]
        dy, dx = dy * length, dx * length
        y, x = y + dy, x + dx
        perimeter += length
        area += x * dy

    return area + (perimeter // 2) + 1


if __name__ == "__main__":
    main()
