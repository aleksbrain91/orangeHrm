import time


def test_lesson_17_drag_and_drop(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Interactions", "Droppable",)
    app.demonstrationAppDemoQa.drag_and_drop()

def test_lesson_17_drop_down_select(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Widgets", "Select Menu")
    app.demonstrationAppDemoQa.select_value_from_old_style_drop_down('White')

def test_lesson_17_upload_file(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Elements", "Upload and Download")
    app.demonstrationAppDemoQa.upload_file('/Users/admin/PycharmProjects/orangeHrm/files/test_upload.txt')

#-----------------------------------------------------------------------------------------

def test_lesson_17_test_drag_and_drop(app):
    app.demonstrationAppDemoQa.openUrl()
    # go to "Interactions" "Dragabble" section
    app.demonstrationAppDemoQa.go_to_side_menu_section("Interactions", "Dragabble",)
    # drag and drop the element to any position from the default from the page
    app.demonstrationAppDemoQa.drag_and_drop_dragabble()
def test_lesson_17_test_drop_down_select(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Widgets", "Select Menu")
    # select any other option from "Select One" drop-down
    app.demonstrationAppDemoQa.select_value_from_select_one_dropdown("Other")


def test_lesson_17_test_upload_file(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Elements", "Upload and Download")
    # Create some file in your project and upload it using upload method from previous example
    app.demonstrationAppDemoQa.upload_my_file(r'C:\Users\Alexbrain\PycharmProjects\orangeHrm\files\some_file.txt')