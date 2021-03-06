_call_count = 0


def next_colour():
    global _call_count
    colour = COLORS[_call_count % len(COLORS)]
    _call_count += 1
    return colour


COLORS = (
    "#1f77b4",  # 10 first ones are the default ones
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
    "sienna",
    "gainsboro",
    "skyblue",
    "c",
    "plum",
    "lightslategrey",
    "peru",
    "darkturquoise",
    "orchid",
    "yellow",
    "wheat",
    "seagreen",
    "mediumaquamarine",
    "hotpink",
    "darkgrey",
    "firebrick",
    "mediumslateblue",
    "coral",
    "olivedrab",
    "navy",
    "darkolivegreen",
    "silver",
    "palegreen",
    "black",
    "slategrey",
    "purple",
    "aqua",
    "crimson",
    "indianred",
    "slategray",
    "indigo",
    "lavenderblush",
    "white",
    "honeydew",
    "olive",
    "azure",
    "darkgray",
    "gold",
    "mintcream",
    "sandybrown",
    "floralwhite",
    "cadetblue",
    "mediumorchid",
    "powderblue",
    "lightskyblue",
    "w",
    "ghostwhite",
    "darkviolet",
    "royalblue",
    "lavender",
    "slateblue",
    "m",
    "y",
    "darkred",
    "dimgrey",
    "orange",
    "violet",
    "lightslategray",
    "darkblue",
    "saddlebrown",
    "bisque",
    "snow",
    "steelblue",
    "darkgreen",
    "cornflowerblue",
    "forestgreen",
    "midnightblue",
    "darkslateblue",
    "turquoise",
    "darkorange",
    "dimgray",
    "darkkhaki",
    "red",
    "maroon",
    "darkslategray",
    "yellowgreen",
    "blueviolet",
    "oldlace",
    "grey",
    "khaki",
    "lightcoral",
    "darkmagenta",
    "lightseagreen",
    "lightpink",
    "salmon",
    "darkgoldenrod",
    "mistyrose",
    "k",
    "lightgray",
    "lightblue",
    "green",
    "orangered",
    "mediumturquoise",
    "lightyellow",
    "darkorchid",
    "mediumblue",
    "lightsalmon",
    "darksalmon",
    "fuchsia",
    "rosybrown",
    "blue",
    "mediumvioletred",
    "g",
    "palegoldenrod",
    "lightcyan",
    "navajowhite",
    "mediumseagreen",
    "pink",
    "papayawhip",
    "darkseagreen",
    "magenta",
    "b",
    "lawngreen",
    "r",
    "chocolate",
    "lightgrey",
    "palevioletred",
    "aliceblue",
    "antiquewhite",
    "lime",
    "cornsilk",
    "whitesmoke",
    "linen",
    "deepskyblue",
    "burlywood",
    "beige",
    "dodgerblue",
    "chartreuse",
    "thistle",
    "aquamarine",
    "gray",
    "springgreen",
    "darkslategrey",
    "mediumspringgreen",
    "blanchedalmond",
    "limegreen",
    "greenyellow",
    "brown",
    "mediumpurple",
    "lightsteelblue",
    "darkcyan",
    "paleturquoise",
    "seashell",
    "rebeccapurple",
    "cyan",
    "tan",
    "peachpuff",
    "moccasin",
    "goldenrod",
    "lightgreen",
    "lightgoldenrodyellow",
    "deeppink",
    "tomato",
    "teal",
    "lemonchiffon",
)
