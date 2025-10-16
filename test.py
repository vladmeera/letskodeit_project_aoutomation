import typing

RED: typing.Final = "RED"
GREEN: typing.Final = "GREEN"
BLUE: typing.Final = "BLUE"

color = RED


match color:
    case "RED":
        print("color is red!")
    case "GREEN":
        print("color is green!")
    case "BLUE":
        print("color is blue")

    case _:
        print("I dont know this color")
        