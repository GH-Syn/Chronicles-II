"""
author: Joshua Rose <joshuarose099@gmail.com>
license: MIT
`torch.py`: This file contains the _Torch_ class.
"""

from abc import ABC


class Torch(ABC):
    """🌈 Torches are guiding lights that illuminate the environment 🔥"""

    def __init__(self, color: str | None = "yellow") -> None:
        """
        The torch has different animations for different colors:
        - amber yellow
        - ethereal blue
        - crimson red
        - forest green

        :param color: The color of the torch - defaults to yellow.
        :type color: str | None
        :rtype: None
        """

        valid_colors = ["yellow", "blue", "green", "red"]

        if color is None:
            self.color = "yellow"
        elif isinstance(color, str) and color in valid_colors:
            self.color = color
        else:
            raise ValueError("A torch color must be yellow, blue, green, or red")
