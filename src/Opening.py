# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl

class Opening:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: mandatory
        # width: mandatory
        # height: mandatory
        # thickness: mandatory
        # color: mandatory        

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            raise Exception('Parameter "position" required.')       
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'thickness' not in self.parameters:
            raise Exception('Parameter "thickness" required.')    
        if 'color' not in self.parameters:
            raise Exception('Parameter "color" required.')  
            
        # Generates the opening from parameters
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
        
        x = self.parameters['position'][0]
        y = self.parameters['position'][1]
        z = self.parameters['position'][2]
        
        self.vertices = [ 
                [0+x, 0+y, 0+z],
                [0+x, 0+y, self.parameters['height']+z],
                [self.parameters['width']+x, 0+y, self.parameters['height']+z],
                [self.parameters['width']+x, 0+y, 0+z],
                [0+x, self.parameters['thickness']+y, 0+z],
                [self.parameters['width']+x, self.parameters['thickness']+y, self.parameters['height']+z],
                [0+x, self.parameters['thickness']+y, self.parameters['height']+z],
                [self.parameters['width']+x, self.parameters['thickness']+y, 0+z]
                ]
        self.faces = [
                [0, 1, 6,4],
                [0, 3, 7 ,4],
                [1, 2, 5, 6],
                [3, 7, 5, 2]
                ]   
        
    # Draws the faces                
    def draw(self):        
        gl.glPushMatrix() 
        gl.glPolygonMode (gl.GL_FRONT_AND_BACK,gl.GL_FILL)
        gl.glBegin(gl.GL_QUADS)
        gl.glColor3fv([0.5,0.5,0.5])        
        for face in self.faces:
            for x in face:
                gl.glVertex3fv(self.vertices[x])
        
        gl.glEnd()        
        gl.glPopMatrix()