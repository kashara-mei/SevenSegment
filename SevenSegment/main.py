from machine import Pin


class SevenSegmentDisplay:
    def __init__(self, pin_map: dict[int, int]):
        self.pins = []

        if len(pin_map) != 8: raise ValueError("Invalid pin map")
        for i in range(1, 9):  # from 1 to 8
            self.pins.append(Pin(pin_map[i], mode=Pin.OUT))

        '''
        draft:
        { 1 : 15 }
        means: GPIO 15 take control over segment 1
        '''

    def set(self, seg_id: int, value: bool) -> None:
        self.pins[seg_id - 1].value(int(value))

    def get(self, seg_id: int) -> bool:
        return bool(self.pins[seg_id - 1].value())

    def toggle(self, seg_id):
        self.set(seg_id, not self.get(seg_id))

    numbers: dict[int, list[int]] = {
        1: [3, 8],
        2: [7, 8, 5, 1, 2],
        3: [7, 8, 5, 3, 2],
        4: [6, 5, 8, 3],
        5: [7, 6, 5, 3, 2],
        6: [6, 1, 2, 3, 5, 7],
        7: [7, 8, 3],
        8: [1, 2, 3, 5, 6, 7, 8],
        9: [2, 3, 5, 6, 7, 8],
        0: [1, 2, 3, 6, 7, 8]
    }

    def light_digit(self, digit: int, add_dot: bool = False) -> None:
        if digit < 0 or digit > 9:
            raise ValueError("Invalid digit value")
        segments = self.numbers[digit].copy()
        if add_dot: segments += [4]
        for i in range(1, 9):
            to_set: bool
            if i in segments:
                to_set = True
            else:
                to_set = False
            self.set(i, to_set)

    def clear(self):
        for i in range(1, 9):
            self.set(i, False)

''' USE EXAMPLE
ssd = SevenSegmentDisplay({1: 16, 2: 17, 3: 18, 4: 19, 5: 15, 6: 14, 7: 13, 8: 12})
work: bool = True
while work:
    inp = input('Enter number to display (0-9)\n> ')
    print()

    if inp == "clear" or int(inp[0]) == -1: ssd.clear(); continue
    ssd.light_digit(int(inp[0]), '.' in inp)
'''


















