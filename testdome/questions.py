def group_by_owners(files: dict) -> dict:
    by_owners = dict()

    for file, owner in files.items():
        if not by_owners.get(owner):
            by_owners[owner] = []

        by_owners[owner].append(file)
    return by_owners


def main():
    files = {
        "Input.txt": "Randy",
        "Code.py": "Stan",
        "Output.txt": "Randy",
        "index.html": "Randy",
    }
    print(group_by_owners(files))


if __name__ == "__main__":
    main()
