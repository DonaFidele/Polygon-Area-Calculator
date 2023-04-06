#coding:utf-8

class Rectangle:

    def __init__(self,width=0, height=0):
        self.width=width
        self.height=height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self,new_width):
        self.width=new_width

    def set_height(self,new_height):
        self.height=new_height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return  2 * (self.width + self.height)
    
    def get_picture (self):
        if self.height>50 or self.width>50:
            return "Too big for picture."
        else:
            picture=''
            for i in range(self.height):
                for i in range(self.width):        
                    picture+='*'             
                picture+='\n'
            return picture

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_amount_inside(self,carre):
        return (self.width//carre.width )*(self.height//carre.height)



class Square(Rectangle):
    def __init__(self,cote=0,width=0, height=0):
        Rectangle.__init__(self,width=0, height=0)
        self.cote=cote
        self.width=cote
        self.height=cote

    def  __repr__(self):
        Rectangle.__repr__(self)
        return f"Square(side={self.cote})"

    def set_side(self,new_side):
        self.cote=new_side
        self.width=new_side
        self.height=new_side
    def set_width(self,new_side):
        self.cote=new_side
        self.width=new_side
        self.height=new_side
    def set_height(self,new_side):
        self.cote=new_side
        self.width=new_side
        self.height=new_side
    
    def get_amount_inside(self,rect):
        return (self.cote//rect.width )*(self.cote//rect.height)


#Usage example

rect =Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
