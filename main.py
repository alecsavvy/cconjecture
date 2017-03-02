import algorithm
import ph
import ch
import ex

def main():
    while True:
        menu = "Run a simulation (1) \n \
               Run a Parental Hierarchy (2) \n \
               Quit (3)"
        cmd = input(menu)
        if cmd == "1":
            ex.run()
            print("end of simulation")
            continue
        elif cmd == "2":
            ph.run()
            print("end of parental hierarchy simulation")
            continue
        elif cmd == "3":
            print("quitting")
            break
        else:
            continue
    return None

def run():
    main()
    return None

run()
