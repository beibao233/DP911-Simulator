
def remove(text: str, chars: list = None):
    if chars is None:
        chars = ['\n', ' ']

    for char in chars:
        text = text.replace(char, "")

    return text


def sim_storage_space(text):
    data = remove(text)

    spaces = []

    for i in range(int(len(data)/2)):
        spaces.append(data[i*2]+data[i*2+1])

    return spaces

