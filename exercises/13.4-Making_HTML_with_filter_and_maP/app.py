all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(color):
    return color["sexy"]
filtered_colors = list(filter(filter_colors, all_colors))

def generate_li(color):
    return "<li>" + color["label"] + "</li>"
generated_li = list(map(generate_li, filtered_colors))
print(generated_li)