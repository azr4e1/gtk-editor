from gtk_editor.src.app import MyApp
import sys


def run():
    app = MyApp(application_id="com.example.GtkApplication")
    app.run(sys.argv)
