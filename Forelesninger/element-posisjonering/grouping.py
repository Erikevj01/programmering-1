import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Grouping", width=400, height=300)

with dpg.window(no_title_bar=True, width=400, height=300):
    dpg.add_text("Temp")
    with dpg.group(horizontal=True):
        dpg.add_button(label="Button")
        dpg.add_text("This is just text.")
        dpg.add_text("This is also just text")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()