class Tile():
    def __init__(self, color, hover_color, has_number: bool = False, number: int = 0, painted: bool = False):
        self.has_number = has_number
        self.number = number
        self.painted = painted
        self.color = color
        self.hover_color = hover_color

    # future features: a game based on the exercise 127 from the book "ginástica cerebral 2", a kind of a minesweeper 2 


    def change_tile(self, color, hover_color):
        if self.painted:
            if color == self.color:
                self.painted = not self.painted
        else:
            self.painted = not self.painted        
        self.color = color
        self.hover_color = hover_color



    def set_color(self, color):
        self.color = color


    
        
    

    
        


    

        

        