from uagame import Window
from time import sleep

# create window
window = Window('Hacking', 600, 500)
window.set_font_color('green')
window.set_font_name('couriernew')
window.set_bg_color('black')
window.set_font_size(18)

line_y = 0
string_height = window.get_font_height()

# displaying attempts left
window.draw_string('1 ATTEMPT(S) LEFT', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height

# displaying password list
window.draw_string('DOG', 0, line_y)
window.update
sleep(0.3)
line_y = line_y + string_height

window.draw_string('CAT', 0, line_y)
window.update
sleep(0.3)
line_y = line_y + string_height

# prompt user for password
sleep(0.3)
guess = window.input_string('ENTER PASSWORD > ', 0, line_y)

# clear window
window.clear()

# create outcome
if guess == 'DOG':
    window.draw_string('PASSWORD SUCCESS', 0, 0)
    window.update()
else:
    window.draw_string('PASSWORD FAILURE', 0, 0)
    window.update()       

sleep(2)

# prompt for end
window.input_string('PRESS ENTER TO QUIT', 0, line_y)

# close window
window.close()