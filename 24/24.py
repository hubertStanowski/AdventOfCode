import os
import sys
from sympy import Symbol, solve_poly_system

# refactored code by https://www.reddit.com/user/Imnimo/, as I didn't know python libraries to do this problem


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        data = f.read().splitlines()

    shards = []
    for line in data:
        pos, vel = line.strip().split(" @ ")
        px, py, pz = map(int, pos.split(", "))
        vx, vy, vz = map(int, vel.split(", "))
        shards.append((px, py, pz, vx, vy, vz))

    print(part1(shards))
    print(part2(shards))


def part1(shards):
    count = 0
    for adx in range(len(shards) - 1):
        shard_a = shards[adx]
        ma = shard_a[4] / shard_a[3]
        ba = shard_a[1] - (ma * shard_a[0])
        for bdx in range(adx + 1, len(shards)):
            shard_b = shards[bdx]
            mb = shard_b[4] / shard_b[3]
            bb = shard_b[1] - (mb * shard_b[0])
            if ma != mb:
                ix = (bb - ba) / (ma - mb)
                iy = (ma * ix) + ba

                ta = (ix - shard_a[0]) / shard_a[3]
                tb = (ix - shard_b[0]) / shard_b[3]

                if ta >= 0 and tb >= 0 and ix >= 200000000000000 and ix <= 400000000000000 and iy >= 200000000000000 and iy <= 400000000000000:
                    count += 1

    return count


def part2(shards):
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    vx = Symbol('vx')
    vy = Symbol('vy')
    vz = Symbol('vz')

    equations = []
    t_symbols = []
    for idx, shard in enumerate(shards[:3]):
        x0, y0, z0, target_vx, target_vy, target_vz = shard
        t = Symbol('t'+str(idx))

        eqx = x + (vx*t) - x0 - (target_vx*t)
        eqy = y + (vy*t) - y0 - (target_vy*t)
        eqz = z + (vz*t) - z0 - (target_vz*t)

        equations.append(eqx)
        equations.append(eqy)
        equations.append(eqz)
        t_symbols.append(t)

    solved = solve_poly_system(equations, *([x, y, z, vx, vy, vz] + t_symbols))

    return sum(solved[0][:3])


if __name__ == "__main__":
    main()
