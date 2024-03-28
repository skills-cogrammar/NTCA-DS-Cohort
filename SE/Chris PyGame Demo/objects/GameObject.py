import pygame

class GameObject:
    def __init__(self, 
                 image_path : str, 
                 x : int, 
                 y : int, 
                 speed : float, 
                 is_player : bool,
                 image_size : tuple[int, int] | None = None, ):
        """
        Starts the passed image at the set x and y pos.
        Speed sets the default speed that the object should move at.
        Is_Player will set if object is a player object or not with a bool value.
        """
        self.image = pygame.image.load(image_path).convert_alpha()
        # Resize the image if image_size is provided
        if image_size is not None:
            self.image = pygame.transform.scale(self.image, image_size)
        self.x = x
        self.y = y
        self.is_player = is_player
        self.speed = speed
        self.x_dir = 0 # stores the x player direction
        self.y_dir = 0 # stores the y player direction

    def reset_movement(self):
        """
        Resets the direction the player was moving
        """
        self.x_dir = 0 
        self.y_dir = 0 

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        # Resets all movement
        self.reset_movement()

    # TODO - Update logic to move object on screen when each method is called
    def move_left(self, clock_tick: int):
        delta_time = clock_tick / 1000.0
        
        # 1 * 0.5 = -0.5
        self.x_dir = -(self.speed * delta_time)
        print("Moving left!")

    def move_right(self, clock_tick: int):
        delta_time = clock_tick / 1000.0
        
        # 1 * 0.5 = 0.5
        self.x_dir = (self.speed * delta_time)
        print("Moving right!")

    def move_up():
        print("Moving up!")

    def move_down():
        print("Moving down!")

    def move(self):
        """
        Updates player position based on selected directions.
        """
        self.x += self.x_dir 
        self.y += self.y_dir 

