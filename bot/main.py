from app.handlers import (
    MemoryStorage,
    router,
    Dispatcher,
    Bot,
    logging,
    asyncio,
)
from app.utils import get_token

# imports for testing
from app.services.script import add_timestamp,remove_last_timestamp
from datetime import *

BOT_TOKEN = get_token()


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

    # testing features
    # add_timestamp('456','Work','Помогите нахуй', datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))
    # remove_last_timestamp('456')
