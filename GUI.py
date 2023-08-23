from tkinter import ttk, Tk, Button, Frame
from PIL import Image, ImageTk

IMAGE_NAMES = ['P', '1', '2', '3', '4', '5', '6', '7', '8', '9']


class Gui:
    def __init__(self, building) -> None:
        self.root = Tk(className="Elevator controller")

        self.building = building

        state = building.get_state()

        self.num_of_floors = len(state[0])

        self.images = []
        for image_name in IMAGE_NAMES:
            url = "./resources/" + image_name + ".png"
            tmp_image = (Image.open(url))
            tmp_image = tmp_image.resize((50, 50), Image.ANTIALIAS)
            self.images.append(ImageTk.PhotoImage(tmp_image))

        url = "./resources/up.png"
        tmp_image = (Image.open(url))
        tmp_image = tmp_image.resize((25, 25), Image.ANTIALIAS)
        up_image = ImageTk.PhotoImage(tmp_image)
        url = "./resources/down.png"
        tmp_image = (Image.open(url))
        tmp_image = tmp_image.resize((25, 25), Image.ANTIALIAS)
        down_image = ImageTk.PhotoImage(tmp_image)

        match self.num_of_floors:
            case 1:
                window_size = "350x200"
            case 2:
                window_size = "350x250"
            case 3:
                window_size = "350x400"
            case 4:
                window_size = "350x450"
            case 5:
                window_size = "350x600"
            case 6:
                window_size = "350x650"
            case 7:
                window_size = "350x800"
            case 8:
                window_size = "350x850"
            case 9:
                window_size = "350x950"
            case _:
                window_size = "350x950"
        self.root.geometry(window_size)

        big_A_Frame = Frame(
            self.root,
            highlightbackground="black",
            highlightthickness=2
        )
        A_Frame = Frame(big_A_Frame)
        big_A_Frame.grid(column=0, row=0, padx=15)
        A_Frame.grid(column=0, row=1)

        big_B_Frame = Frame(
            self.root,
            highlightbackground="black",
            highlightthickness=2
        )
        B_Frame = Frame(big_B_Frame)
        big_B_Frame.grid(column=1, row=0, padx=15)
        B_Frame.grid(column=0, row=1)

        floors_Frame = Frame(
            self.root,
            highlightbackground="black",
            highlightthickness=2
        )
        floors_Frame.grid(column=0, row=1, pady=25)

        indicators_frame = []
        indicators_frame = Frame(
            self.root,
            highlightbackground="black",
            highlightthickness=2
        )
        indicators_frame.grid(column=1, row=1)

        floors = []
        self.floor_buttons = []
        self.A_buttons = []
        self.B_buttons = []

        A_indicator_frames = []
        B_indicator_frames = []
        self.A_indicator_buttons_up = []
        self.A_indicator_buttons_down = []
        self.B_indicator_buttons_up = []
        self.B_indicator_buttons_down = []

        image_ind = self.num_of_floors-1
        for i in range(self.num_of_floors):
            floors.append(Frame(
                floors_Frame,
                highlightbackground="black",
                highlightthickness=2
            ))
            floors[i].grid(column=0, row=i+1, padx=0)

            self.floor_buttons.append(Button(
                floors[i],
                image=self.images[image_ind],
                command=lambda m=['f', i]: self.execute_state_change(m)
            ))
            self.floor_buttons[i].grid(column=0, row=i)

            # ---------------
            A_indicator_frames.append(Frame(
                indicators_frame,
                highlightbackground="black",
                highlightthickness=2
            ))
            A_indicator_frames[i].grid(column=0, row=i+1, padx=10, pady=13)

            self.A_indicator_buttons_up.append(Button(
                A_indicator_frames[i],
                image=up_image
            ))
            self.A_indicator_buttons_up[i].grid(column=0, row=i)
            ttk.Label(
                A_indicator_frames[i],
                text='A',
                font='Helvetica 15 bold'
            ).grid(column=1, row=i)
            self.A_indicator_buttons_down.append(Button(
                A_indicator_frames[i],
                image=down_image
            ))
            self.A_indicator_buttons_down[i].grid(column=2, row=i)

            B_indicator_frames.append(Frame(
                indicators_frame,
                highlightbackground="black",
                highlightthickness=2
            ))
            B_indicator_frames[i].grid(column=1, row=i+1)

            self.B_indicator_buttons_up.append(Button(
                B_indicator_frames[i],
                image=up_image
            ))
            self.B_indicator_buttons_up[i].grid(column=0, row=i)
            ttk.Label(
                B_indicator_frames[i],
                text='B',
                font='Helvetica 15 bold'
            ).grid(column=1, row=i)
            self.B_indicator_buttons_down.append(Button(
                B_indicator_frames[i],
                image=down_image
            ))
            self.B_indicator_buttons_down[i].grid(column=2, row=i)
            # ---------------

            image_ind -= 1

        ttk.Label(
            big_A_Frame,
            text="Elevator A",
            font='Helvetica 13 bold'
        ).grid(column=0, row=0)
        ttk.Label(
            big_B_Frame,
            text="Elevator B",
            font='Helvetica 13 bold'
        ).grid(column=0, row=0)
        ttk.Label(
            floors_Frame,
            text="Floors: ",
            font='Helvetica 13 bold'
        ).grid(column=0, row=0)
        ttk.Label(
            indicators_frame,
            text="Indicators: ",
            font='Helvetica 13 bold'
        ).grid(column=0, row=0)

        image_ind = self.num_of_floors-1
        add_row = False
        row = 1
        for i in range(self.num_of_floors):
            if image_ind == 1:
                self.A_buttons.append(Button(
                    A_Frame,
                    image=self.images[image_ind],
                    command=lambda m=['A', i]: self.execute_state_change(m)
                ))
                self.A_buttons[i].grid(column=i % 2 + 1, row=row)
            else:
                self.A_buttons.append(Button(
                    A_Frame,
                    image=self.images[image_ind],
                    command=lambda m=['A', i]: self.execute_state_change(m)
                ))
                self.A_buttons[i].grid(column=i % 2 + 1, row=row)
            if not add_row:
                add_row = True
            else:
                row += 1
                add_row = False
            image_ind -= 1

        image_ind = self.num_of_floors-1
        add_row = False
        row = 1
        for i in range(self.num_of_floors):
            if image_ind == 1:
                self.B_buttons.append(Button(
                    B_Frame,
                    image=self.images[image_ind],
                    command=lambda m=['B', i]: self.execute_state_change(m)
                ))
                self.B_buttons[i].grid(column=i % 2, row=row)
            else:
                self.B_buttons.append(Button(
                    B_Frame,
                    image=self.images[image_ind],
                    command=lambda m=['B', i]: self.execute_state_change(m)
                ))
                self.B_buttons[i].grid(column=i % 2, row=row)
            if not add_row:
                add_row = True
            else:
                row += 1
                add_row = False
            image_ind -= 1

        self.floor_buttons.reverse()
        self.A_buttons.reverse()
        self.B_buttons.reverse()

        self.refresh_window()

        self.root.mainloop()

    def refresh_window(self):
        state = self.building.get_state()

        for button in self.A_buttons:
            button.config(state="normal")
        for button in self.B_buttons:
            button.config(state="normal")
        for button in self.floor_buttons:
            button.config(state="normal")

        for index, floor in enumerate(state[0]):
            if floor:
                self.floor_buttons[index].config(state="disabled")

        self.A_buttons[state[1]
                       [0].floor].config(state="disabled")
        self.B_buttons[state[1]
                       [1].floor].config(state="disabled")

        if state[1][0].get_moving_down():
            for indicator_button in self.A_indicator_buttons_down:
                indicator_button.config(state="disabled")
        elif state[1][0].get_moving_up():
            for indicator_button in self.A_indicator_buttons_up:
                indicator_button.config(state="disabled")
        else:
            for indicator_button in self.A_indicator_buttons_down:
                indicator_button.config(state="normal")
            for indicator_button in self.A_indicator_buttons_up:
                indicator_button.config(state="normal")

        if state[1][1].get_moving_down():
            for indicator_button in self.B_indicator_buttons_down:
                indicator_button.config(state="disabled")
        elif state[1][1].get_moving_up():
            for indicator_button in self.B_indicator_buttons_up:
                indicator_button.config(state="disabled")
        else:
            for indicator_button in self.B_indicator_buttons_down:
                indicator_button.config(state="normal")
            for indicator_button in self.B_indicator_buttons_up:
                indicator_button.config(state="normal")

        self.root.update()
        self.root.update_idletasks()

    def move_elevator(self, elevator_index, move_by):
        if move_by < 0:
            self.building.elevators[elevator_index].set_moving_down()
            for i in range(abs(move_by)):
                self.building.move_elevator_down(elevator_index)
                self.refresh_window()
            self.building.elevators[elevator_index].unset_moving_down()
            self.refresh_window()
        else:
            self.building.elevators[elevator_index].set_moving_up()
            for i in range(move_by):
                self.building.move_elevator_up(elevator_index)
                self.refresh_window()
            self.building.elevators[elevator_index].unset_moving_up()
            self.refresh_window()

    def call_elevator(self, floor):
        elevator_index = self.building.select_elevator(floor)
        if elevator_index == -1:
            print("Wrong floor number!")
            return
        move_by = floor - self.building.elevators[elevator_index].get_floor()
        self.move_elevator(elevator_index, move_by)

    def send_elevator(self, elevator_index, floor):
        if floor > self.num_of_floors-1 or floor < 0:
            print("Wrong floor number!")
            return
        move_by = floor - self.building.elevators[elevator_index].get_floor()
        self.move_elevator(elevator_index, move_by)

    def execute_state_change(self, button_data):
        if button_data[0] == 'f':
            self.call_elevator(self.num_of_floors-1-button_data[1])
        elif button_data[0] == 'A':
            self.send_elevator(0, self.num_of_floors-1-button_data[1])
        elif button_data[0] == 'B':
            self.send_elevator(1, self.num_of_floors-1-button_data[1])
