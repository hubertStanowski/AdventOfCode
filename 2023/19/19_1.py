import os
import sys

# not working


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        workflows, parts = f.read().split("\n\n")
        workflows = workflows.split("\n")
        parts = parts.split("\n")
        processed_workflows = {}
        processed_parts = []
        result = 0

        for workflow in workflows:
            label, condtions = process_workflow(workflow)
            processed_workflows[label] = condtions

        for part in parts:
            processed_parts.append(process_part(part))

        for part in processed_parts:
            current_workflow = "in"
            conditions = processed_workflows[current_workflow]
            print(conditions)
            i = 0
            while True:
                condition, value = conditions[i]
                if condition == "no":
                    current_workflow = value
                    if value not in "AR":
                        conditions = processed_workflows[value]
                else:
                    condition = condition.replace("x", str(part.x))
                    condition = condition.replace("m", str(part.m))
                    condition = condition.replace("a", str(part.a))
                    condition = condition.replace("s", str(part.s))
                    if eval(condition):
                        current_workflow = value
                        if value not in "AR":
                            conditions = processed_workflows[value]
                    else:
                        i += 1
                if current_workflow == "A":
                    result += part.rating()
                    break
                elif current_workflow == "R":
                    break

        print(result)


class Part():
    def __init__(self, x=None, m=None, a=None, s=None):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def rating(self):
        return sum([self.x, self.m, self.a, self.s])


def process_workflow(workflow):
    processed = []
    label, conditions = workflow.replace("}", "").split("{")
    conditions = [condition.split(":") for condition in conditions.split(",")]
    for condition in conditions:
        if len(condition) == 2:
            processed.append((condition[0], condition[1]))
        else:
            processed.append(("no", condition[0]))

    return (label, processed)


def process_part(part):
    processed = Part()
    part = part.replace("{", "").replace("}", "").split(",")
    part = [att.split("=") for att in part]
    processed.x = int(part[0][1])
    processed.m = int(part[1][1])
    processed.a = int(part[2][1])
    processed.s = int(part[3][1])

    return processed


if __name__ == "__main__":
    main()
