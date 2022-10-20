import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Elements", width=600, height=400)

with dpg.window(label="Content", width=600, height=400):
    dpg.add_text("This is a text!")
    dpg.add_input_text(label="Input text here", width=150)
    dpg.add_input_int(label="Input int here", width=150)
    dpg.add_input_float(label="Input float here", width=150)
    dpg.add_button(label="Click me")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()