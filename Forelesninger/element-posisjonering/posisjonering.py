import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Positioning", width=400, height=300)

with dpg.window(no_title_bar=True, width=400, height=300):
    dpg.add_button(label="Some element", indent=100)
    dpg.add_text("This is just text", indent=100)

    dpg.add_button(label="This is a button", pos=(200, 200))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
