import pygame

pygame.init() #--> This is a must to run after loading pygame 
#This command create a window for gaming
gameWindow = pygame.display.set_mode((1920,1080))

#This command set the title for the game window.
pygame.display.set_caption("My First Game")

exit = False

#The game loop starts and continues
while not exit:
    #Taking series of input from the user:
    for instructions in pygame.event.get():
        #If the instruction given to computer or you click the close button of the window than the program closes.
        if instructions.type == pygame.QUIT:
            exit = True

        #If the instruction given to computer is through keyboard key than this condition statisfy.
        if instructions.type == pygame.KEYDOWN:
            #If the instruction given is the right key.(Above condition is givenn to avoid error when key input is not given)
            if instructions.key == pygame.K_RIGHT:
                print("You press the right key.")
            elif instructions.key == pygame.KEYUP:
                print("You pressed the left key.")
            else:
                print("You did not press the right or left key.")

#To quit pygame:
pygame.quit()
#To quit the code file:
quit()