import pgzrun
# from pgzero.actor import Actor

WIDTH = 800
HEIGHT = 600
apple = Actor( "apple" )
apple1 = Actor('apple')


def draw():
    screen.clear()
    apple.draw()
    apple1.draw()

def update():
    if apple.x < WIDTH:
        apple.x = apple.x + 1
    else:
        if apple.y < HEIGHT:
            apple.y = apple.y + 1

    if apple1.y < HEIGHT:
        apple1.y = apple1.y + 1
    else:
        if apple1.x < WIDTH:
            apple1.x = apple1.x + 1

pgzrun.go()