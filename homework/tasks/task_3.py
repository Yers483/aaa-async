import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    # Необходимо выполнить все полученные корутины,
    # затем упорядочить их результаты
    # по полю number и вернуть строку, состоящую из склеенных полей key.
    #
    # Пример:
    # r1 = Ticket(number=2, key='мыла')
    # r2 = Ticket(number=1, key='мама')
    # r3 = Ticket(number=3, key='раму')
    #
    # Результат: 'мамамылараму'
    #
    # YOUR CODE GOES HERE
    tickets = await asyncio.gather(*coros)
    tickets = sorted(tickets, key=lambda x: x.number)

    return ''.join([ticket.key for ticket in tickets])
