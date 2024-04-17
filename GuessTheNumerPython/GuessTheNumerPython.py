"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.flex(

        rx.image(src="/1.jpg", width="320px", height="auto",border_radius="8px" ),
        
        rx.flex(
            rx.heading("Welcome to the", font_size="1rem", font_family="Madimi One"),
            rx.heading("Guessing Game!", weight="bold",font_size="2rem", font_family="Madimi One"),
            rx.text("Tray to guess the number I am thinking of between 1 and 100.", 
                    font_size="1rem", 
                    font_family="Madimi One", 
                    align="center", 
                    as_="p"),
            direction="column",
            width="320px",
            align="center"
            # spacing="3",
        ),
        rx.flex(
            rx.input(placeholder="Enter your guess", max_length="20", size="20px", weight="bold", font_family="Madimi One",font_size="1rem"),

        ),
        align="center",
        direction="column",
        size="1",
        margin="20px",
        
    )

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Madimi+One&display=swap",
    ],
)
# app = rx.App(
#     stylesheets=[
#         "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&family=Rubik:ital,wght@0,300..900;1,300..900&display=swap" rel="stylesheet",  # This path is relative to assets/
#     ],
# )
app.add_page(index)
