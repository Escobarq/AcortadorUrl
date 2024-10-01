import flet as ft
import pyshorteners

def button_clicked(e, input_field ,outpud_field):
    input_field = input_field.value
    url_shor = shorten_url()
    outpud_field.value =  url_shor.tinyurl.short(input_field)
    e.page.update()

def shorten_url():
    url_shor =  pyshorteners.Shortener()
    return url_shor

def main(page: ft.Page):
    page.title = "Acortador URL"
    input_field = ft.TextField(label="Insertar URL")
    outpud_field = ft.TextField(label="Nuevo URL",)
    b = ft.ElevatedButton(text="Submit", on_click=lambda e: button_clicked(e, input_field,outpud_field))
    page.add(input_field, outpud_field, b)

ft.app(main)


