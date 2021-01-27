#! /bin/echo 'This file is not meant to be run...'
from tkinter import *
from sys import exit
from libcolor import *


def rect_mid(x, y, h, w):
    return x - w // 2, y - h // 2, x + w // 2, y + h // 2


class Coordinate:
    """ A simple two-value array."""
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_tuple(self):
        return self.x, self.y


class RigidBox:
    """ pd - primary direction. Applied first while calculating movement. Could be "up", "down", "left", "right"
        sd - secondary direction. Applied after pd. Could be used to create diagonal movement
        center - a Coordinate (tm) that represents the box center
        width, height - width and height of the box
        x_velo, y_velo - x and y axis velocity
        box - a Tk object label (to manipulate) (shouldn't be created)
        canvas - the Tk canvas to manipulate (should be created)"""
    pd = "up"
    sd = "left"
    center = Coordinate(0, 0)
    width = 1
    height = 1
    x_velo = 2
    y_velo = 2
    box = -1
    color = Color(0, 0, 0)

    def __init__(self, w, h, c, pd, sd, vx, vy, canvas):
        self.width = w
        self.height = h
        self.center = c
        self.x_velo = vx
        self.y_velo = vy
        self.canvas = canvas
        if pd != "up" and pd != "down" and pd != "left" and pd != "right":
            self.pd = pd
        else:
            exit("Unreadable direction in pd")
        
        if sd != "up" and sd != "down" and sd != "left" and sd != "right":
            self.sd = sd
        else:
            exit("Unreadable direction in sd")
        self.box = self.canvas.create_rectangle(rect_mid(self.center.to_tuple(), self.width, self.height),
        fill=self.color.to_hex(), outline=self.color.to_hex())

    def reset(self):
        self.canvas.delete(self.box)
        self.box = self.canvas.create_rectangle(rect_mid(self.center.to_tuple(), self.width, self.height),
        fill=self.color.to_hex(), outline=self.color.to_hex())

    def animate(self, *boxes):
        return "Work in progress"
