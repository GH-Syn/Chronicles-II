"""
About
-----
`__main__.py` exists so the following command(s) can be run:

```bash
python src
```

This is preferable to a file-level entry.
```bash
cd src
python file.py
```

A folder level entry allows easier relative path grepping to `res`; removing the need for manual inserts into system path variables.
"""

import sys
import loguru
import pygame

from utils.io_handler import get_parser, set_logging_level

parser = get_parser()

parser.add_argument(
    "--debug",
    action="store_true",
    help="Show debugging log level messages for developers",
)

def main():
    args = parser.parse_args()

    level = "INFO" if not args.debug else "DEBUG"
    set_logging_level(level)

    window = pygame.display.set_mode()

if __name__ == "__main__":
    main()
