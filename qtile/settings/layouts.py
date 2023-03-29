# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

from libqtile import layout
from libqtile.config import Match
from .theme import colors

# Layouts and layout rules


layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 2,
    'margin': 4
}

layout_conf2 = {
    'border_focus': colors['focus'][0],
    'border_width': 2,
}

layout_conf3 = {
    'border_width': 2,
}

layouts = [
    layout.Max(**layout_conf2, margin=[4, 4, 4, 4]),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.MonadThreeCol(**layout_conf),
    layout.TreeTab(
        **layout_conf3,
        font='Comic Code Ligatures',
        fontsize=13,
        sections=['α', 'β', 'γ', 'δ'],
        section_fontsize=13,
        bg_color='0f101a',
        active_bg='a151d3',
        inactive_bg='4c566a',
        padding_left=0,
        margin_left=4,
        padding_x=0,
        padding_y=5,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=100
    ),
    layout.Matrix(columns=2, **layout_conf),
    layout.RatioTile(**layout_conf),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
        Match(wm_class='font-manager'),
        Match(wm_class='pavucontrol'),
        Match(wm_class='Arandr'),
        Match(wm_class='feh'),
        Match(wm_class='Galculator'),
        Match(wm_class='notification'),
        Match(wm_class='file_progress'),
        Match(wm_class='zoom'),
        Match(wm_class='megasync'),
        Match(wm_class='com.devspace.javafxproject.App')
    ],
    border_focus=colors["color4"][0]
)
