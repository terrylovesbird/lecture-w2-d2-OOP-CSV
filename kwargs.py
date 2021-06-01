my_dict = {
    "donuts": "yummy",
    "green_beans": "gross"
}

def my_func(bagels, green_beans):
    print(bagels, green_beans)

my_func(my_dict["donuts"], my_dict["green_beans"])
my_func(**my_dict)
my_func(green_beans="gross", donuts="yummy")