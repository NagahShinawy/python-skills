def group_by_owners(files: dict) -> dict:
    by_owners = dict()

    for file, owner in files.items():
        if not by_owners.get(owner):
            by_owners[owner] = []

        by_owners[owner].append(file)
    return by_owners


class DictHelper:
    def __init__(self, container: dict):
        self.container = container

    def group_by_value(self):
        by_value = dict()

        for key, value in self.container.items():
            if not by_value.get(value):
                by_value[value] = []

            by_value[value].append(key)
        return by_value
    
    def extend(self, **kwargs):
        self.container.update(**kwargs)
        return self.container


def main():
    files = {
        "Input.txt": "Randy",
        "Code.py": "Stan",
        "Output.txt": "Randy",
        "index.html": "Randy",
    }
    print(group_by_owners(files))
    helper = DictHelper(files)
    print(helper.group_by_value())
    
    print(files.pop("index.html"))
    print(files)
    print(helper.extend(test="test", ))


if __name__ == "__main__":
    main()
