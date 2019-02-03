# -*- coding: utf-8 -*-
"""The main entry point.

Invoke as `myapp` or `python -m myapp`.
"""
import sys


def main() -> None:
    try:
        from .app import main
        sys.exit(main())
    except KeyboardInterrupt:
        from . import ExitStatus
        sys.exit(ExitStatus.ERROR_CTRL_C)


if __name__ == '__main__':
    main()
