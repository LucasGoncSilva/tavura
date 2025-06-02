from argparse import ArgumentParser, Namespace, RawDescriptionHelpFormatter
from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING, basicConfig, getLogger
from typing import Final, cast

from rich.logging import RichHandler

from .metadata import *  # noqa: F403


def set_logging_config(v: int = 3) -> None:
    """
    Configures the logging level for the application based on the provided verbosity.

    Logging is handled using `RichHandler` for enhanced terminal output. The verbosity
    level `v` controls the logging granularity for the `tavura` logger.

    :param v: Verbosity level, from 0 (critical) to 4 (debug). Defaults to 3 (info).
        - 0: Critical
        - 1: Error
        - 2: Warning
        - 3: Info
        - 4: Debug
    :type v: int
    :returns: None.
    :rtype: None
    """

    basicConfig(
        format='%(message)s',
        handlers=[RichHandler()],
    )

    match v:
        case 0:
            getLogger('tavura').setLevel(CRITICAL)
        case 1:
            getLogger('tavura').setLevel(ERROR)
        case 2:
            getLogger('tavura').setLevel(WARNING)
        case 3:
            getLogger('tavura').setLevel(INFO)
        case 4:
            getLogger('tavura').setLevel(DEBUG)
        case _:
            getLogger('tavura').setLevel(INFO)


def main() -> None:
    """
    This is the script's entrypoint, kinda where everything starts.

    It takes no parameters inside code itself, but uses ArgumentParser to deal with
    them. Parsing the args, extracts the infos provided to deal and construct the
    output doc based on them.

    :rtype: None
    """

    # Parser Creation
    parser: ArgumentParser = ArgumentParser(
        description=(__doc__),
        formatter_class=RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        '--states',
        type=str,
        nargs='+',
        default=['Committed', 'Test', 'Review'],
        help='List of states to be tracked: New, Approved, '
        'Committed, External, Test, Accepted, Review, Done.',
    )
    parser.add_argument(
        '--headless',
        type=bool,
        default=True,
        help='Defines if browser should be emulated or not.',
    )
    parser.add_argument(
        '--verbose',
        type=int,
        default=3,
        help='Verbosity level, from 0 (quiet/critical) to 4 (overshare/debug).',
    )

    # Arguments Parsing
    args: Namespace = parser.parse_args()

    set_logging_config(args.verbose)

    logger = getLogger('tavura')
    logger.info('Logger config done')

    STATES: list[str] = args.states
    logger.debug(f'{STATES = }')
    expected: Final[list[str]] = [
        'New',
        'Approved',
        'Committed',
        'External',
        'Test',
        'Accepted',
        'Review',
        'Done',
    ]
    if any(map(lambda x: x.strip().title() not in expected, STATES)):
        raise RuntimeError(
            f'Every state in "--states" must be in {expected}, got {STATES}.'
        )

    HEADLESS: list[str] = args.headless
    logger.debug(f'{HEADLESS = }')

    logger.info('Arguments parsed successfully')

    if HEADLESS:
        from os import environ

        environ['HEADLESS'] = 'True'

    # Codebase Reading
    from app.system.constants import MAIL, PASS
    from app.system.manager import Manager

    logger.info('Starting process')
    Manager.run_pipeline(cast(str, MAIL), cast(str, PASS), STATES)


if __name__ == '__main__':
    main()
