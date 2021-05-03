import turtle

DEFAULT_SIDE = 10


def draw_triangle(pen, l):
	for i in range(0,3):
		pen.forward(l)
		pen.left(120)
	return None

def draw_recursive(pen, l, N, i=0):
	
	# draw
	if i <= N:

		big_L = 2**i * l
		draw_triangle(pen, big_L)

		draw_recursive(pen, l, N, i+1)

	# stop
	else:
		pass

	return (N, i)


def main():

	turtle.clear()
	my_window = turtle.Screen()
	my_pen = turtle.Turtle()

	#draw_triangle(my_pen, DEFAULT_SIDE)
	draw_recursive(my_pen, DEFAULT_SIDE, 4)

if __name__ == "__main__":
	main()

