import random

def main():
    NUM_SIDES = int(input("How many sides does your dice have?:"))    
    dice = random.randint(1, NUM_SIDES)
    print("Your roll is " + str(dice))

if __name__ == '__main__':
    main()
