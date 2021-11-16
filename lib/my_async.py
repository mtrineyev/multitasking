import logging
import asyncio

counters = (
    ('Counter-1', 5, 2),
    ['Counter-2', 5, 1],
    ('Counter-3', 5, 1),
)


async def my_counter(name: str, n: int, pause=1) -> None:
    """
    async counter prints numbers from 1 to n with pausing in 1 sec
    :param name: name of the counter
    :param n: number of iterations
    :param pause: pause between iterations in sec
    :return: None
    """
    logging.info(
        f'{name} will count to {n} with {pause} sec pause')
    for i in range(n):
        logging.info(f'{name} says {i + 1}')
        await asyncio.sleep(pause)
    logging.info(f'{name} has been finished')


async def my_asyncio(infinite=False, loop=None):
    """
    Run three counters consistently, infinite or parallel using asyncio
    :param infinite: boolean, run second counter infinite
    :param loop: async loop, if None run counters consistently
    :return:
    """
    as_inf = 10000
    if infinite:
        counters[1][1] = as_inf
    if not loop:
        for name, count, pause in counters:
            await asyncio.create_task(my_counter(name, count, pause))
    else:
        await asyncio.wait([
            loop.create_task(my_counter(name, count, pause))
            for name, count, pause in counters
        ])
