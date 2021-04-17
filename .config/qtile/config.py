from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget

from typing import List # noqa: F401

mod = "mod4"

keys = [
    # QTile
    Key(
        [mod, "control"], "r",
        lazy.restart()
    ),
    Key(
        [mod, "control"], "q", 
        lazy.shutdown()
    ),
    Key(
        [mod, "shift"], "c", 
        lazy.window.kill()
    ),
    # Screen
    Key(
        [mod, "control"], "j",
        lazy.next_screen()
    ),
    Key([mod, "control"], "k",
        lazy.prev_screen()
    ),
    # Layout
    Key(
        [mod], "Tab", 
        lazy.next_layout()
    ),
    Key(
        [mod], "j", 
        lazy.layout.down()
    ),
    Key(
        [mod], "k", 
        lazy.layout.up()
    ),
    Key(
        [mod, "shift"], "j",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "shift"], "k", 
        lazy.layout.shuffle_up()
    ),
    Key(
        [mod, "shift"], "Return", 
        lazy.layout.toggle_split() 
    ),
    Key(
        [mod], "h",
        lazy.layout.shrink_main(),
    ),
    Key(
        [mod], "l",
        lazy.layout.grow_main(),
    ),
    # Application
    Key(
        [mod], "r",
        lazy.spawncmd()
    ),
    Key(
        [mod], "Return", 
        lazy.spawn("alacritty")
    ),
]

groups = [Group(name, **kwargs) for name, kwargs in [
    ("u", {
        "label": "dev",
        "layout": "max",
        "layouts": [layout.MonadTall(), layout.Max()],
    }),
    ("i", {
        "label": "sys",
        "layout": "monadtall",
        "layouts": [layout.MonadTall(), layout.MonadWide()],
        "spawn": ["alacritty", "alacritty"]
    }),
    ("o", {
        "label": "www",
        "layout": "max",
        "layouts": [layout.Max()],
        "spawn": ["qutebrowser"]
    }),
    ("m", {
        "label": "cht",
        "layout": "max",
        "layouts": [layout.Max(), layout.MonadTall(), layout.MonadWide()],
        "spawn": ["element-desktop"]
    }),
    ("n", {
        "label": "etc",
        "layout": "monadtall",
        "layouts": [layout.Stack(), layout.MonadTall(), layout.MonadWide()],
    }),
    #("0", {
    #    "label": "mus",
    #    "layout": "max",
    #    "layouts": [layout.Max()],
    #    "spawn": ["alacritty -e vimpc", "alacritty -e pulsemixer"]
    #}),
]]

for group in groups:
    keys.extend([
        Key([mod], group.name, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], group.name, lazy.window.togroup(group.name))
    ])

widget_defaults = dict(
    font="monospace",
    fontsize=12,
    padding=3,
)
screens = [
    Screen(),
    Screen(
        bottom = bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(),
                widget.Notify(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
            ],
            24,
        ),
    ),
]

follow_mouse_focus = False
cursor_warp = True
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
floating_layout = layout.Floating(float_rules=[
    {"wmclass": "confirm"},
    {"wmclass": "dialog"},
    {"wmclass": "download"},
    {"wmclass": "error"},
    {"wmclass": "file_progress"},
    {"wmclass": "notification"},
    {"wmclass": "splash"},
    {"wmclass": "toolbar"},
    {"wmclass": "confirmreset"}, # gitk
    {"wmclass": "makebranch"}, # gitk
    {"wmclass": "maketag"}, # gitk
    {"wname": "branchdialog"}, # gitk
    {"wname": "pinentry"}, # GPG key password entry
    {"wmclass": "ssh-askpass"}, # ssh-askpass
])

# XXX: Gasp! We"re lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn"t work correctly. We may as well just lie
# and say that we"re a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java"s whitelist.
wmname = "LG3D"
