def group_by_owners(files: dict) -> dict:
    by_owners = dict()

    for file, owner in files.items():
        if not by_owners.get(owner):
            by_owners[owner] = []

        by_owners[owner].append(file)
    return by_owners


class DictMixin:
    def __init__(self, container: dict):
        self.container = container

    def group_by_value(self):
        by_value = dict()

        for key, value in self.container.items():
            if not by_value.get(value):
                by_value[value] = []

            by_value[value].append(key)
        return by_value

    def __len__(self):
        return len(self.container.keys())


def main():
    files = {
        "Input.txt": "Randy",
        "Code.py": "Stan",
        "Output.txt": "Randy",
        "index.html": "Randy",
    }
    print(group_by_owners(files))
    dic_helper = DictMixin(files)
    print(dic_helper.group_by_value())
    print(len(dic_helper))


if __name__ == "__main__":
    main()
