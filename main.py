"""
The script for testing multitasking using threading and asyncio modules

1. Consistently run three counters using threading
2. Parallel run three counters using threading, one counter is infinite
3. Parallel run three counters using threading
or
4. Consistently run three counters using asyncio
5. Parallel run three counters using asyncio, one counter is infinite
6. Parallel run three counters using asyncio
"""

import logging
import asyncio

from lib.my_threads import my_threading
from lib.my_async import my_asyncio

correct_choices = ('1', '2', '3', '4', '5', '6')
logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S'
)


def main() -> None:
    """
    The main script for testing multitasking
    :return: None
    """
    print(__doc__)
    while True:
        try:
            choice = input('Enter your choice: ')
            if choice in correct_choices:
                break
        except KeyboardInterrupt:
            print('Terminated')
            exit(1)
    logging.info('Starting counters...\n******************************')
    loop = asyncio.get_event_loop()
    if choice == '1':
        my_threading(consistently=True)
    elif choice == '2':
        my_threading(infinite=True)
    elif choice == '3':
        my_threading()
    elif choice == '4':
        asyncio.run(my_asyncio())
    elif choice == '5':
        loop.run_until_complete(my_asyncio(infinite=True, loop=loop))
    elif choice == '6':
        loop.run_until_complete(my_asyncio(loop=loop))
    logging.info('Main function is finished')


if __name__ == '__main__':
    main()
