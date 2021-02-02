import pygame
import time
import math


class Player:
    def __init__(self, _x, _y, _size, _window, _map):
        self.body = pygame.Rect(_x, _y, _size, _size)
        self.color = (26, 7, 109)
        self.__speed = 3
        self.__window = _window
        self.__grounded = False
        self.__isJumping = False
        self.__mass = 0.2
        self.__jumpImpulse = 15
        self.actualImpulse = 0
        self.map = _map

    def draw(self):
        pygame.draw.rect(self.__window, self.color, self.body)

    def MovePlayer(self, Direction):
        if Direction == "Left":
            self.body = self.body.move(-self.__speed, 0)
        elif Direction == "Right":
            self.body = self.body.move(self.__speed, 0)

    def isJumping(self):
        return self.__isJumping

    def isGrounded(self):
        if self.body.collidelistall(self.map):
            self.__grounded = True
        else:
            self.__grounded = False
        return self.__grounded

    def fall(self, g):
        if self.isGrounded():
            self.__isJumping = False
            return False

        elif self.isJumping():
            self.actualImpulse += self.__mass * g
            self.body = self.body.move(0, self.actualImpulse)

        else:
            self.body = self.body.move(0, self.__mass * g)
        return True

    def Jump(self):
        self.actualImpulse = -self.__jumpImpulse
        self.__isJumping = True
        self.body = self.body.move(0, self.actualImpulse)
