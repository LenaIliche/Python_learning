from draw_menu import *
from draw_start import *

window = Tk()

window.geometry('1200x600')
window.title("Крестики-нолики против компа")

menu = Menu(window)
draw_menu(window, menu)

draw_start_and_play(window)

window.mainloop()
