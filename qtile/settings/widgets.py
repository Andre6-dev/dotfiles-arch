from libqtile import qtile, widget
from libqtile.config import Drag, Click
from libqtile.command import lazy
from .theme import colors
import os

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

mod = "mod4"


def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def iconScript(fg='text', bg='dark', fontsize=18, text="?", script="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=4,
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(os.path.expanduser(script))}
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",  # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )


def image(filename='?', script='?'):
    return widget.Image(
        filename=os.path.expanduser(filename),
        scale='False',
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(os.path.expanduser(script))},
        padding=5,
    )


def workspaces():
    return [
        separator(),
        image(filename='~/.config/qtile/assets/dragon1.png', script='~/.config/rofi/launchers/type-6/launcher.sh'),
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=17, padding=5, max_chars=50),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color8', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color8'), scale=0.65),

    widget.CurrentLayout(**base(bg='color8'), padding=5),

    powerline('color4', 'color8'),

    icon(bg="color4", text=' '),  # Icon: nf-fa-download

    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerline('color7', 'color4'),

    widget.Memory(**base(bg='color7'), format='溜 {MemUsed: .0f}M', padding=5),

    powerline('color6', 'color7'),

    icon(bg="color6", text='󰈀 '),  # Icon: nf-fa-feed

    widget.Net(**base(bg='color6'), interface='enp4s0'),

    powerline('color1', 'color6'),

    icon(bg="color1", fontsize=17, text=' '),  # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color1'),

    image(filename='~/.config/qtile/assets/sweetlogo.png', script='~/.config/rofi/powermenu/type-6/powermenu.sh'),

    widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color8', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color8'), scale=0.65),

    widget.CurrentLayout(**base(bg='color8'), padding=5),

    powerline('color2', 'color8'),

    icon(bg="color2", fontsize=17, text=' '),  # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),

    image(filename='~/.config/qtile/assets/sweetlogo.png', script='~/.config/rofi/powermenu/type-6/powermenu.sh'),

    iconScript(fg='color5', bg="dark", text=' ', script='pavucontrol &'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

extension_defaults = widget_defaults.copy()
