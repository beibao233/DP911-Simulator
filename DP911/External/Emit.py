from DP911.Registers.Variables import Variable


bases = {
    '01': ("hex", "0x", 4, 4),
    '02': ("", "", 5, 3),
    '03': ("oct", "0o", 6, 3),
    '04': ("bin", "0b", 16, 4)
}


def main(data: tuple, web_mode: bool = False):
    unprocessed = \
        list(eval(f"str({bases[data[1]][0]}({Variable.read(data[0])})).replace('{bases[data[1]][1]}', '', 1)"))

    for _ in range(bases[data[1]][2] - len(unprocessed)):
        unprocessed.insert(0, '0')

    for i in range(int(bases[data[1]][2] / bases[data[1]][3])):
        unprocessed.insert((i * bases[data[1]][3]) + i, ' ')

    if unprocessed[0] == ' ':
        unprocessed.pop(0)

    processed = ''.join(unprocessed).upper()

    if not web_mode:
        print(processed)

    base = bases[data[1]][0]

    if base == '':
        base = 'dec'

    return f"输出{base}进制的{processed}"
