def mask_line(line):
    if line == "":
        return ""
    words = line.split(" ")
    return " ".join(["_" for _ in range(len(words))])