import os

# OLD → NEW
CLASS_MAP = {
    0: 0,  # person
    1: None,  # gun → drop
    2: None,
    3: 1,  # knife
    4: 0,  # knife_attacker → person
    5: 0,  # person
    6: None,
    7: None,
    8: None
}


LABEL_DIRS = [
    "backend/app/datasets/weapons/train/labels",
    "backend/app/datasets/weapons/valid/labels",
    "backend/app/datasets/weapons/test/labels",
]

for label_dir in LABEL_DIRS:
    for file in os.listdir(label_dir):
        if not file.endswith(".txt"):
            continue

        path = os.path.join(label_dir, file)
        new_lines = []

        with open(path, "r") as f:
            lines = f.readlines()

        for line in lines:
            parts = line.strip().split()
            old_class = int(parts[0])

            if CLASS_MAP[old_class] is None:
                continue  # drop label

            parts[0] = str(CLASS_MAP[old_class])
            new_lines.append(" ".join(parts))

        with open(path, "w") as f:
            f.write("\n".join(new_lines))
