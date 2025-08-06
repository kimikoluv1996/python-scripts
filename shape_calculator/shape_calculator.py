import argparse

# works like 'shape_calculator --width 100 --height 100'
# or 'shape_calculator --area 1000 --width 100' 

parser = argparse.ArgumentParser(
    prog="shape_calculator", 
    description="calculates the area of various shapes"
)

parser.add_argument('--width')
parser.add_argument('--height')
parser.add_argument('--base')
parser.add_argument('--radius')
parser.add_argument('--area')

def calculate_area():
    list_args = parser._get_args()
    """ if list_args[0] == 100:
        area = 10
    else: area = 20 """
    #return area

print(parser._get_args())
#print(f"area is {calculate_area()}")