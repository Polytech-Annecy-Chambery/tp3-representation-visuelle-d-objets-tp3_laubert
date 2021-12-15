# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self     

    # Defines the vertices and faces 
    def generate(self):        
        self.vertices = [ 
                [0, 0, 0 ],
                [self.parameters['width'],0,0],
                [0,self.parameters['thickness'],0],
                [0, 0, self.parameters['height']],
                [self.parameters['width'], self.parameters['thickness'],0],
                [self.parameters['width'], 0, self.parameters['height']],
                [0, self.parameters['thickness'], self.parameters['height']],
                [self.parameters['width'], self.parameters['thickness'], self.parameters['height']]
                ]
        self.faces = [
                [0, 1, 5, 3],
                [1, 4, 7, 5],
                [4, 2, 6, 7],
                [2, 0, 3, 6],
                [3, 5, 7, 6],
                [0, 1, 4, 2]
                ]   
    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        if x.parameters['width']+x.parameters['position'][0]<= self.parameters['position'][0]+self.parameters['width']:
            if x.parameters['height']+x.parameters['position'][2]<=self.parameters['position'][2]+self.parameters['height']:
                return True
            return False
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
        # A compléter en remplaçant pass par votre code
        pass              
        
    # Draws the edges
    def drawEdges(self):
        gl.glPushMatrix() 
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE)        
        gl.glBegin(gl.GL_QUADS)
        gl.glColor3fv([0.2,0.2,0.2])
        self.setParameter('position',[0,0,0])
        self.setParameter('orientation',0)
        
        for elem in self.faces:
           for vertex in elem:
                  gl.glVertex3fv(self.vertices[vertex])
        
        gl.glEnd()        
        gl.glPopMatrix()       
                 
                    
    # Draws the faces
    def draw(self):
        gl.glPushMatrix() 
        gl.glPolygonMode (gl.GL_FRONT_AND_BACK,gl.GL_FILL)
        gl.glBegin(gl.GL_QUADS)
        gl.glColor3fv([0.5,0.5,0.5])
        self.setParameter('position',[0,0,0])
        self.setParameter('orientation',0)
        
        for face in self.faces:
            for x in face:
                gl.glVertex3fv(self.vertices[x])
        
        gl.glEnd()        
        gl.glPopMatrix()
        
        
        #Draw if
        for j in self.objects:
            j.draw()
        if self.parameters['edges'] :
            self.drawEdges()
        
         
        
  