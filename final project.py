# Carlos Perez Rosas, Adrian Cadena 12/12/2022
# U.S. Air Pollution Checker
# Program will allow the user to look into pollution data in states and create graphs to illustrate pollution and
# comparisons between states. Program will also allow user to choose and look at individual state graphs from 2000-2021

import tkinter
import tkinter.messagebox
import tkinter.ttk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def exit_gui():
    """ends the program"""
    root.destroy()
    plt.close('all')


# All function hover events are shown below
# Opens hover event
def label_hover(event):
    """Hover event for year_input"""
    new_label.grid(row=2, column=0)  # add label to the grid


# Removes Hover event
def label_hover_end(event):
    """Removes hover event for year_input"""
    new_label.grid_remove()  # remove label from the grid


# Function for State Comparison button
def comparison():
    """State Comparison Function"""
    # Will destroy previous GUI
    root.destroy()
    # Global variables for use in other functions
    global second_root
    global new_label
    global year_input
    global amount_combo
    global pollution

    # State Comparison GUI is made
    second_root = tkinter.Tk()
    second_root.title("U.S. Air Pollution Checker")
    second_root.configure(bg="light blue")
    second_root.geometry("830x300")

    # Year label for GUI
    year_label = tkinter.Label(second_root, text="Enter Year")
    year_label.grid(row=0, column=0)
    year_label.configure(bg="Light green", font="bold")

    # Entry box for user is made here
    year_input = tkinter.Entry(second_root, width=10)
    year_input.grid(row=1, column=0, padx=10, pady=0, sticky="w")
    year_input.configure(width=20, font="bold")

    # Hover event is bound to entry box
    year_input.bind("<Enter>", label_hover)
    year_input.bind("<Leave>", label_hover_end)

    # Label for GUI illustrating Amount of States is made here
    state_label = tkinter.Label(second_root, text="Amount of States")
    state_label.grid(row=0, column=2)
    state_label.configure(bg="Light green", font="bold")

    # State selection combo box is created here
    state_amount = [*range(5, 16, 5)]
    amount_combo = tkinter.ttk.Combobox(second_root, values=state_amount, state="readonly")
    amount_combo.current(0)
    amount_combo.grid(row=1, column=2, pady=10, padx=10)
    amount_combo.configure(font="bold")

    # Hover event label created here
    new_label = tkinter.Label(second_root, text="Enter from years 2000-2021!")
    new_label.configure(bg="yellow")
    new_label.configure(font="Arial 10 italic bold", )

    # Pollution label for GUI created here
    pollution_label = tkinter.Label(second_root, text="Pollution Type")
    pollution_label.grid(row=0, column=3)
    pollution_label.configure(bg="Light green", font="bold")

    # Pollution type combo box is created here
    pollution_type = ['Ground-Level Ozone', 'Carbon Monoxide', 'Sulfur Dioxide', 'Nitrogen Dioxide']
    pollution = tkinter.ttk.Combobox(second_root, values=pollution_type, state="readonly")
    pollution.current(0)
    pollution.grid(row=1, column=3, pady=10, padx=10)
    pollution.configure(font="bold")

    # Button that will execute the comparison is made here
    check_button = tkinter.Button(second_root, text="Compare", command=check)
    check_button.grid(row=1, column=4, padx=5, sticky="w")
    check_button.configure(bg="Light green", width=15, height=1, font="bold", pady=10, padx=10)

    # Return button which will let the user go back to previous GUI will be created here
    return_button = tkinter.Button(second_root, text="Return", command=back_button)
    return_button.grid(row=2, column=4, padx=5, sticky="w", pady=10)
    return_button.configure(bg="salmon", width=15, height=1, font="bold", pady=10, padx=10)

    # Shows the legend for Air Quality Index
    legend_label = tkinter.Label(second_root, text="Air Quality Index Legend")
    legend_label.configure(bg="light green", height=1, font="bold")
    legend_label.grid(row=2, column=2, sticky="e")
    label = tkinter.Label(second_root, text="Good")
    label.configure(bg="green", fg="white", font="bold")
    label.grid(row=3, column=2, sticky="e")
    label2 = tkinter.Label(second_root, text="Moderate")
    label2.configure(bg="yellow", fg="black", font="bold")
    label2.grid(row=4, column=2, sticky="e")
    label3 = tkinter.Label(second_root, text="sensitive")
    label3.configure(bg="orange", fg="black", font="bold")
    label3.grid(row=5, column=2, sticky="e")
    label4 = tkinter.Label(second_root, text="unhealthy")
    label4.configure(bg="red", fg="white", font="bold")
    label4.grid(row=6, column=2, sticky="e")
    label5 = tkinter.Label(second_root, text="Very unhealthy")
    label5.configure(bg="darkred", fg="white", font="bold")
    label5.grid(row=7, column=2, sticky="e")
    label6 = tkinter.Label(second_root, text="Hazardous")
    label6.configure(bg="purple", fg="white", font="bold")
    label6.grid(row=8, column=2, sticky="e")

    second_root.mainloop()


def back_button():
    """Function to go back to previous GUI"""
    # Global variable for use in other functions
    global root

    # Will destroy current GUI and recreate first GUI for new selection
    second_root.destroy()
    root = tkinter.Tk()
    root.title("U.S. Air Pollution Checker")
    root.configure(bg="Grey")
    root.geometry("760x105")

    # Will create button to execute State Comparison GUI
    top_states = tkinter.Button(root, text="State Comparison", command=comparison)
    top_states.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    top_states.configure(bg="orange", font="bold", width=25, height=4)

    # Will create button to execute Single State Search GUI
    custom_search = tkinter.Button(root, text="Single State Search", command=single_state)
    custom_search.grid(row=0, column=3, padx=10, pady=10, sticky="w")
    custom_search.configure(bg="orange", font="bold", width=25, height=4)

    # exit GUI button
    exit_search = tkinter.Button(root, text="Exit", command=exit_gui)
    exit_search.grid(row=0, column=4, padx=10, pady=10, sticky="w")
    exit_search.configure(bg="salmon", font="bold", width=25, height=4)

    root.mainloop()


# Will read csv file globally
dataframe = pd.read_csv('simple pollution file_2000_2021.csv', index_col='Year')


def check():
    """Compare button function"""
    # try block will check for errors
    try:
        # Will convert entries into assigned values
        year_int = int(year_input.get())
        pollution_str = str(pollution.get())
        state_int = int(amount_combo.get())

        # if statement will check that values entered are  positive
        if year_int >= 0 and state_int >= 0:

            # if statement will check that values are within scope
            if 2021 >= year_int >= 2000:

                # if, elif's and else will trigger depending on what pollution was selected
                # and assign variable to placeholder
                if pollution_str == "Ground-Level Ozone":
                    pollution_tag = 'O3 AQI'
                elif pollution_str == "Carbon Monoxide":
                    pollution_tag = 'CO AQI'
                elif pollution_str == "Sulfur Dioxide":
                    pollution_tag = 'SO2 AQI'
                else:
                    pollution_tag = 'NO2 AQI'

                # This will grab all pollution sets withing given year
                sorted_data = dataframe[dataframe.index == year_int].sort_values(by=pollution_tag, ascending=False)
                # Will select specified amount of states
                state = sorted_data['State'].head(state_int)
                # Will sort data to display on the graph
                amount = sorted_data[pollution_tag].head(state_int)

                # this for loop will assign a color depending on pollution scale,
                # green for minimal to purple for hazardous
                colors = []
                for value in amount:
                    if value <= 50:
                        colors.append('green')
                    elif 50 < value <= 100:
                        colors.append('yellow')
                    elif 100 < value <= 150:
                        colors.append('orange')
                    elif 150 < value <= 200:
                        colors.append('red')
                    elif 200 < value <= 300:
                        colors.append('darkred')
                    else:
                        colors.append('purple')

                year_input.delete(0, tkinter.END)

                # this displays bar graphs based on user input year, amount of states, and pollution type
                tkinter.messagebox.showinfo("Success", "Graph created successfully!")
                year_string = str(year_int)
                plt.figure(figsize=(18, 5), dpi=100)
                plt.suptitle(pollution_str, weight="bold")
                plt.title("Year: " + year_string, weight="bold", loc="center")
                plt.bar(state, amount, color=colors)
                plt.xlabel("U.S. States", weight="bold")
                plt.ylabel("Air Quality Index", weight="bold")
                plt.show()

            else:
                # else will trigger if value entered is out of scope
                tkinter.messagebox.showerror("Error", "Entry out of scope, please choose between years 2000 and 2021!")
                year_input.delete(0, tkinter.END)
        else:
            # else will happen if negative value is entered
            tkinter.messagebox.showerror("Error", "There should only be positive numeric values!")
            year_input.delete(0, tkinter.END)

    except:
        # If something other than numeric values is entered it will trigger except and message box
        tkinter.messagebox.showerror("Error", "Please make sure that only numeric values are entered.")
        year_input.delete(0, tkinter.END)


def single_state():
    """ this function opens if the user chooses to search one state"""
    global third_root
    global year_input2
    global state_box
    global pollution2
    root.destroy()
    third_root = tkinter.Tk()
    third_root.title("U.S. Air Pollution Checker")
    third_root.configure(bg="light blue")
    third_root.geometry("620x320")

    states_label = tkinter.Label(third_root, text="Choose State")
    states_label.grid(row=0, column=2, padx=10, pady=10)
    states_label.configure(bg="Light green", font="bold")

    # removes  duplicate states and appends into a list for combobox
    get_state = dataframe.drop_duplicates('State')
    get_state = get_state.sort_values('State', ascending=True)
    get_state = get_state['State']
    state_list = get_state.values.tolist()

    # GUI combo box configuration
    state_box = tkinter.ttk.Combobox(third_root, values=state_list, state="readonly")
    state_box.current(0)
    state_box.grid(row=1, column=2, pady=10, padx=10, sticky="w")
    state_box.configure(font="bold")

    pollution_label2 = tkinter.Label(third_root, text="Pollution Type")
    pollution_label2.grid(row=0, column=3)
    pollution_label2.configure(bg="Light green", font="bold")
    pollution_type2 = ['Ground-Level Ozone', 'Carbon Monoxide', 'Sulfur Dioxide', 'Nitrogen Dioxide']
    pollution2 = tkinter.ttk.Combobox(third_root, values=pollution_type2, state="readonly")
    pollution2.current(0)
    pollution2.grid(row=1, column=3, pady=10, padx=10)
    pollution2.configure(font="bold")

    # GUI label configurations
    new_label2 = tkinter.Label(third_root, text="Enter from years 2000-2021!")
    new_label2.configure(bg="yellow")
    new_label2.configure(font="Arial 10 italic bold", )

    new_label3 = tkinter.Label(third_root, text="Choose from up to 47 States!")
    new_label3.configure(bg="yellow")
    new_label3.configure(font="Arial 10 italic bold", )

    enter_button = tkinter.Button(third_root, text="Enter", command=enter)
    enter_button.grid(row=1, column=4, padx=5, sticky="w")
    enter_button.configure(bg="Light green", width=15, height=1, font="bold", pady=10, padx=10)

    return_button = tkinter.Button(third_root, text="Return", command=back_button2)
    return_button.grid(row=2, column=4, padx=5, sticky="w", pady=10)
    return_button.configure(bg="salmon", width=15, height=1, font="bold", pady=10, padx=10)

    # Shows the legend for Air Quality Index
    legend_label = tkinter.Label(third_root, text="Air Quality Index Legend")
    legend_label.configure(bg="light green", height=1, font="bold")
    legend_label.grid(row=2, column=2, sticky="e")
    label = tkinter.Label(third_root, text="Good")
    label.configure(bg="green", fg="white", font="bold")
    label.grid(row=3, column=2, sticky="e")
    label2 = tkinter.Label(third_root, text="Moderate")
    label2.configure(bg="yellow", fg="black", font="bold")
    label2.grid(row=4, column=2, sticky="e")
    label3 = tkinter.Label(third_root, text="sensitive")
    label3.configure(bg="orange", fg="black", font="bold")
    label3.grid(row=5, column=2, sticky="e")
    label4 = tkinter.Label(third_root, text="unhealthy")
    label4.configure(bg="red", fg="white", font="bold")
    label4.grid(row=6, column=2, sticky="e")
    label5 = tkinter.Label(third_root, text="Very unhealthy")
    label5.configure(bg="darkred", fg="white", font="bold")
    label5.grid(row=7, column=2, sticky="e")
    label6 = tkinter.Label(third_root, text="Hazardous")
    label6.configure(bg="purple", fg="white", font="bold")
    label6.grid(row=8, column=2, sticky="e")


def back_button2():
    """ returns to main GUI page if user decides to change search"""
    global root
    third_root.destroy()
    root = tkinter.Tk()
    root.title("U.S. Air Pollution Checker")
    root.configure(bg="Grey")
    root.geometry("760x105")

    top_states = tkinter.Button(root, text="State Comparison", command=comparison)
    top_states.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    top_states.configure(bg="orange", font="bold", width=25, height=4)

    custom_search = tkinter.Button(root, text="Single State Search", command=single_state)
    custom_search.grid(row=0, column=3, padx=10, pady=10, sticky="w")
    custom_search.configure(bg="orange", font="bold", width=25, height=4)

    exit_search = tkinter.Button(root, text="Exit", command=exit_gui)
    exit_search.grid(row=0, column=4, padx=10, pady=10, sticky="w")
    exit_search.configure(bg="salmon", font="bold", width=25, height=4)

    root.mainloop()


def enter():
    """enter button function for single state search"""
    state_box_str = str(state_box.get())
    pollution2_str = str(pollution2.get())

    # if, elif's and else will trigger depending on what pollution was selected
    # and assign variable to placeholder
    if pollution2_str == "Ground-Level Ozone":
        pollution_tag2 = 'O3 AQI'
    elif pollution2_str == "Carbon Monoxide":
        pollution_tag2 = 'CO AQI'
    elif pollution2_str == "Sulfur Dioxide":
        pollution_tag2 = 'SO2 AQI'
    else:
        pollution_tag2 = 'NO2 AQI'

    # these three lines filter out any rows that do not have the matching state the user entered,
    # then sorts by the specified pollution type
    sorted_data = dataframe[dataframe['State'] == state_box_str].sort_values(pollution_tag2)
    amount = sorted_data[pollution_tag2].values
    year = sorted_data.index

    # this for loop will assign a color depending on pollution scale,
    # green for minimal to purple for hazardous
    colors = []
    for value in amount:
        if value <= 50:
            colors.append('green')
        elif 50 < value <= 100:
            colors.append('yellow')
        elif 100 < value <= 150:
            colors.append('orange')
        elif 150 < value <= 200:
            colors.append('red')
        elif 200 < value <= 300:
            colors.append('darkred')
        else:
            colors.append('purple')

    # resizes graph window and Displays bar graphs based on chosen state and pollution type
    tkinter.messagebox.showinfo("Success", "Graph created successfully!")
    plt.figure(figsize=(18, 5), dpi=100)
    plt.bar(year, amount, color=colors)
    plt.title(state_box_str, weight="bold")
    plt.xlabel("Years", weight="bold")
    plt.ylabel("Air Quality Index", weight="bold")
    plt.xticks(np.arange(2000, 2022, step=1))
    plt.show()


# Main GUI window when user starts the program
root = tkinter.Tk()
root.title("U.S. Air Pollution Checker")
root.configure(bg="Grey")
root.geometry("760x105")

top_states = tkinter.Button(root, text="State Comparison", command=comparison)
top_states.grid(row=0, column=0, padx=10, pady=10, sticky="w")
top_states.configure(bg="orange", font="bold", width=25, height=4)

custom_search = tkinter.Button(root, text="Single State Search", command=single_state)
custom_search.grid(row=0, column=3, padx=10, pady=10, sticky="w")
custom_search.configure(bg="orange", font="bold", width=25, height=4)

exit_search = tkinter.Button(root, text="Exit", command=exit_gui)
exit_search.grid(row=0, column=4, padx=10, pady=10, sticky="w")
exit_search.configure(bg="salmon", font="bold", width=25, height=4)

root.mainloop()
