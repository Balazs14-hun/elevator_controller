from elevator import Elevator
from string import ascii_uppercase as auc
import time

class Building:
    def __init__(self, num_of_floors, num_of_elevators) -> None:
        if num_of_floors <= 0:
            print("There should be at least 1 floor in the building!")
            return
        if num_of_elevators <= 0:
            print("There should be at least 1 elevator!")
            return
        self.num_of_floors = num_of_floors
        self.num_of_elevators = num_of_elevators

        self.elevators = []
        self.floors = [0] * self.num_of_floors

        elevator_position = 0
        for elevator_index in range(self.num_of_elevators):
            if elevator_position == 0:
                self.floors[elevator_position] += 1
                self.elevators.append(Elevator(elevator_position,
                                               auc[elevator_index]))
                elevator_position = self.num_of_floors-1
            else:
                self.floors[elevator_position] += 1
                self.elevators.append(Elevator(elevator_position,
                                               auc[elevator_index]))
                elevator_position = 0

    def select_elevator(self, floor) -> int:
        if floor > self.num_of_floors-1:
            return -1
        if floor < 0:
            return -1
        elevator_index = 0
        elevator_floor = self.elevators[elevator_index].get_floor()
        best = 1000000
        for index, elevator in enumerate(self.elevators):
            elevator_score = abs(floor - elevator.get_floor())
            if elevator_score == 0:
                elevator_index = index
                break
            if elevator_score < best:    
                elevator_index = index
                best = elevator_score
            elif elevator_score == best:
                if elevator.get_floor() < elevator_floor:
                    elevator_index = index
                    best = elevator_score

        return elevator_index

    def move_elevator_up(self, elevator_index):
        self.floors[self.elevators[elevator_index].get_floor()] -= 1
        self.elevators[elevator_index].move_up()
        self.floors[self.elevators[elevator_index].get_floor()] += 1
        print(self.__str__())
        time.sleep(1)

    def move_elevator_down(self, elevator_index):
        self.floors[self.elevators[elevator_index].get_floor()] -= 1
        self.elevators[elevator_index].move_down()
        self.floors[self.elevators[elevator_index].get_floor()] += 1
        print(self.__str__())
        time.sleep(1)

    def get_state(self):
        state = (self.floors, self.elevators)
        return state

    def __str__(self) -> str:
        to_return = ""
        floor_number = self.num_of_floors - 1
        for floor in self.floors[::-1]:
            to_return += "F" + str(floor_number) + ": " + str(floor) + "\n"
            floor_number -= 1
        for elevator in self.elevators:
            to_return += str(elevator) + "\n"
        return to_return
