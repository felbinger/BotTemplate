from PyDrocsid.material_colours import MaterialColours, NestedInt


class Colours(MaterialColours):
    # General
    default = MaterialColours.teal
    error = MaterialColours.red
    warning = MaterialColours.yellow[700]

    # Cogs

    # Commands
    changelog = NestedInt(
        MaterialColours.teal,
        {
            "report": MaterialColours.yellow[800],
            "warn": MaterialColours.yellow["a200"],
            "mute": MaterialColours.yellow[600],
            "unmute": MaterialColours.green["a700"],
            "kick": MaterialColours.orange[700],
            "ban": MaterialColours.red[500],
            "unban": MaterialColours.green["a700"],
        },
    )
    github = MaterialColours.teal[800]
    info = MaterialColours.indigo
    ping = MaterialColours.green["a700"]
    prefix = MaterialColours.indigo
    stats = MaterialColours.green
    userlog = MaterialColours.green["a400"]
    version = MaterialColours.indigo
