import dearpygui.dearpygui as dpg

def button_print():
    print("This button works!")

dpg.create_context()
dpg.create_viewport(title="My dearest button", width=600, height=400)

with dpg.window(no_title_bar=True, no_move=True,width=600, height=400):
    dpg.add_button(label="Click me!", callback=button_print)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()