# -*- coding: utf-8 -*-

import sys

from argparse import ArgumentParser, ArgumentTypeError
from collections import namedtuple

from lyricli.exceptions import ConsoleException, ParserException
from lyricli.melon import get_lyrics
from lyricli.output import print_out, print_err
from lyricli.__init__ import __version__

Command = namedtuple("Command", ["name", "description", "arguments"])
CLIENT_WEBSITE = ""

COMMANDS = [
    Command(
        name="lyrics",
        description="가사 정보를 보여줍니다.",
        arguments=[
            (["-t", "--title"], {
                "help": "노래 제목",
                "type": str,
            }),
            (["-r", "--artist"], {
                "help": "가수 이름",
                "type": str,
            })
        ]
    )
]

COMMON_ARGUMENTS = [
    (["--debug"], {
        "help": "show debug log in console",
        "action": 'store_true',
        "default": False,
    }),
    (["--no-color"], {
        "help": "disable ANSI colors in output",
        "action": 'store_true',
        "default": False,
    })
]


def get_parser():
    description = "멜론에서 노래 가사를 가져오는 간단한 스크립트"
    parser = ArgumentParser(
        prog="lyricli", description=description, epilog=CLIENT_WEBSITE)
    parser.add_argument(
        "--version", help="현재 버전 정보를 알려줍니다.", action="store_true")

    subparsers = parser.add_subparsers(title="commands")

    for command in COMMANDS:
        sub = subparsers.add_parser(command.name, help=command.description)
        
        sub.set_defaults(func=get_lyrics)

        for args, kwargs in command.arguments + COMMON_ARGUMENTS:
            sub.add_argument(*args, **kwargs)

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    if args.version:
        print("lyricli v{}".format(__version__))
        return

    if "func" not in args:
        parser.print_help()
        return

    try:
        args.func(args)
    except ConsoleException as e:
        print_err(e)
        sys.exit(1)
    except KeyboardInterrupt:
        print_err("Operation canceled")
        sys.exit(1)
    except ParserException as e:
        print_err(e)
        sys.exit(1)

if __name__ == '__main__':
    main()