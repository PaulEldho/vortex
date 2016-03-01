from visual import *
class Cube:
    '''def __init__(self,length_box,height_box,width_box,angle_rot):
        self.length_box=1
        self.height_box=1
        self.width_box=1
        self.angle_rot=0
        '''
#module for box object
    f= frame()
    v= frame()
    i=2
    cube = box(frame = f,pos=(1,0,0),length=1,width=1,height=1,color=color.white)
    def operation(length_box,height_box,width_box):
        while i>=0:
            """length_box=int(raw_input("enter length"))
            height_box=int(raw_input("enter height "))
            width_box=int(raw_input("enter width"))
            angle_rot=int(raw_input("enter the angle in radians"))"""
            cube.length = length_box
            cube.width = width_box
            cube.height = height_box
            #cube.rotate(angle=angle_rot, axis=(0,1,0), origin=cube.pos)
            i=i-1



