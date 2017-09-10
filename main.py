import board

# TODO GUI:
#   - move buttons
#   - quit
#   - reset
#   - solve (requires a whole new function)



def main():

    # Ask user for board size
    try:
        rows = int(input("Enter number of board rows: "))
        cols = int(input("Enter number of board columns: "))
    except ValueError:
        print("User error. Forcing size to 4*4")
        rows = 4
        cols = 4

    # Create a new board and draw it
    board1 = board.Board(rows, cols)
    board1.draw()

    cmd = ""
    while cmd != "q":
        cmd = input("Move empty tile [u]p, [d]own, [l]eft or [r]ight, "
                    "[s]huffle the board or [q]uit. ")
        if cmd in ["u", "d", "l", "r"]:
            board1.move(cmd)
            board1.draw()
        elif cmd == "s":
            try:
                shufflecount = int(input("Enter number of random moves: "))
            except ValueError:
                print("User error. Forcing random move count to 100.")
                shufflecount = 100
            board1.shuffle(shufflecount)
            board1.draw()
        elif cmd == "q":
            break
        else:
            print("Unknown command, please try again")
main()
