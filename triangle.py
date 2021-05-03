import turtle

DEFAULT_SIDE = 10

def draw_triangle(pen, l, rotate=0):
	# triangle or triangle-like motif!
	R = (rotate + 1) % 3 

	for i in range(0,3):
		if i == R:
			pen.forward(l/2)
			pen.left(60)
			pen.forward(l/2)
			pen.backward(l/2)
			pen.right(60)
			pen.forward(l/2)

		else:
			pen.forward(l)
			
		pen.left(120)

	return None

def move_to_start(pen, l, i):

	pen.penup()

	if i<=0:
		pass

	else:
		move_to_start(pen,l,i-1)
		
		pen.left(120)
		pen.forward(l * 2**(i-1))
		pen.right(180)

	return i

def draw_generation(pen, l, i, r=0):
	# generation = i

	pen.pendown()

	if i <= 0:
		draw_triangle(pen, l, r)

	else:
		for n in range(0,3):
			draw_generation(pen, l, i-1, r-n)
			pen.forward(2**i * l)
			pen.left(120)

		# now fill in centre
		pen.forward(2**(i-1) * l)
		pen.left(60)
		draw_generation(pen, l, i-1, r)

		# restore position
		pen.right(60)
		pen.backward(2**(i-1) * l)


	return i


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

	generations = 6

	my_window = turtle.Screen()
	my_window.clear()
	my_pen = turtle.Turtle()
	my_pen.speed(0)

	move_to_start(my_pen, DEFAULT_SIDE, generations)
	draw_generation(my_pen, DEFAULT_SIDE, generations)

	deleteme = raw_input("press any key to exit")

	return None

if __name__ == "__main__":
	main()

