
import aiohttp


async def request_json(param: dict) -> list | dict | None:
    '''
    Получаем весь json  либо None
    '''
    try:
        async with aiohttp.request(**param) as resp:
            if resp.status == 200:
                return await resp.json(content_type=None)
    except Exception as e:
        print('request_json : ', e)



def date_str_to_datetime(date: str, hours: int = None, minute: int = None) -> datetime | None:
    '''
    Получаем строку даты "год, месяц, день" (порядок важен),
    создаем объект datetime, можно передать часы и минуты
    по умолчанию 0 часов, 0 минут
    '''
    num = list(map(int, re.findall(r'\d+', date)))
    if len(num) == 3:
        hours = hours if hours else 0
        minute = minute if minute else 0
        return datetime(*num, hours, minute)

