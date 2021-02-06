#  Copyright (C) 2021 AlexiWolf
#
#  This file is part of gladiator_game.
#
#  gladiator_game is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  gladiator_game is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with gladiator_game.  If not, see <https://www.gnu.org/licenses/>.

import sys
from random import randint

import pygame


class Vector:
    """A simple 2D Vector."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, value):
        return Vector(self.x * value, self.y * value)

    @property
    def all(self):
        return self.x, self.y

    @all.setter
    def all(self, new):
        self.x, self.y = new.all


def main():
    # Engine setup.
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Hello, World!")
    clock = pygame.time.Clock()
    frame_rate = 60
    frame_time = 1 / frame_rate

    # Font / message initialization.
    font = pygame.font.SysFont(None, 64)
    message = font.render("Hello, World!", True, (255, 255, 255))

    # Animation initialization.
    screen_center = Vector(screen.get_width() // 2, screen.get_height() // 2)
    message_location = screen_center
    message_velocity = Vector(randint(-200, 200), randint(-200, 200))

    # Main game loop.
    while True:

        # Tick the message's angle of rotation by 3 degrees each frame.
        # The loop restarts when finished.
        for angle in range(0, 361, 2):

            # Process events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

            # Draw the background.
            screen.fill((0, 0, 0))

            # Rotate the message by the current angle, and find it's new center.
            rotated_message = pygame.transform.rotate(message, angle)
            message_center = Vector(
                rotated_message.get_width() // 2, rotated_message.get_height() // 2
            )

            # Move the image in the current direction, scaling the update to the frame
            # time.
            message_location += message_velocity * frame_time

            # Rectangle locations are from the top left corner by default, so this
            # adjustment is required for the message to spin around it's center-point
            # instead of around it's top left corner.
            centered_message_location = message_location - message_center

            # Draw the rotated message at its current location.
            screen.blit(rotated_message, centered_message_location.all)

            # Bounce off the sides of the screen.
            if message_location.x <= 0 or message_location.x >= screen.get_width():
                message_velocity.x *= -1
                message_velocity.y += randint(-1, 1) * 0.1
            if message_location.y <= 0 or message_location.y >= screen.get_height():
                message_velocity.y *= -1
                message_velocity.y += randint(-1, 1) * 0.1

            # Show the frame on screen.
            pygame.display.update()

            # Wait for next display update.
            clock.tick(frame_rate)


if __name__ == "__main__":
    sys.exit(main())
