class Elevator:
    def __init__(self, floor, name) -> None:
        self.name = name
        self.floor = floor
        self.moving_up = False
        self.moving_down = False

    def get_floor(self) -> int:
        return self.floor

    def set_moving_up(self):
        self.moving_up = True

    def unset_moving_up(self):
        self.moving_up = False

    def set_moving_down(self):
        self.moving_down = True

    def unset_moving_down(self):
        self.moving_down = False

    def get_moving_up(self) -> bool:
        return self.moving_up

    def get_moving_down(self) -> bool:
        return self.moving_down

    def move_down(self):
        self.floor -= 1

    def move_up(self):
        self.floor += 1

    def __str__(self) -> str:
        to_return = "Elevator " \
                    + str(self.name) \
                    + " is on the " \
                    + str(self.floor) \
                    + ". floor."
        return to_return
