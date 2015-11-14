class GhostTrack:

    def __init__(self):
        self.list_size = 0
        self.current_pos = 0
        self.pos_list = []

    def add_pos(self, ang, rad):
        self.list_size += 1
        self.pos_list.append((ang, rad))

    def get_next_pos(self):
        if self.list_size == self.list_size:
            self.current_pos += 1
        return self.pos_list[self.current_pos-1];

    def reset_count(self):
        self.current_pos = 0;


if __name__ == '__main__':
    h = GostTrack()
    h.add_pos(20, 30)
    h.add_pos(34, 76)
    print(h.get_next_pos())
    print(h.get_next_pos())
    h.reset_count()
    print(h.get_next_pos())
    print(h.get_next_pos())
