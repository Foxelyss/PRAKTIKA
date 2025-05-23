# SyncInAsync uses only built-in libraries, you can just download this .py and use it in your projects!
# https://github.com/PogoDigitalism/SyncInAsync

import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Any
from functools import partial


class SyncInAsync:
    def __init__(self, POOL: ThreadPoolExecutor = None):
        """
        Requires an existing and active event loop.

        POOL: [Optional] Include a preset ThreadPoolExecutor, will create a default ThreadPoolExecutor otherwise (with the max amount of max_workers)

        The default max_workers amount is os.cpu_count() * 5

        """
        self._POOL = POOL or ThreadPoolExecutor()
        self._LOOP = asyncio.get_event_loop()

        self._result = None

    def __setattrs(func):
        async def async_wrapped(*args, **kwargs):
            self = args[0]
            self._ARGS = args
            self._KWARGS = kwargs
            self._result = None

            return await func(*args, **kwargs)

        def wrapped(*args, **kwargs):
            self = args[0]
            self._ARGS = args
            self._KWARGS = kwargs

            return func(*args, **kwargs)

        if asyncio.iscoroutinefunction(func):
            return async_wrapped
        else:
            return wrapped

    def __Exceptions(self, _):
        """
        Not functional.
        """
        try:
            pass
        except asyncio.exceptions.CancelledError:
            Warning('You are cancelling the future!')

    @__setattrs
    def Wrap(self, func: Callable, *args, **kwargs) -> asyncio.Task:
        """
        func: Your synchronous function, you can pass regular and keyword arguments in this method.

        example: SIA.Wrap(ImageGenerator, CONFIG.Sizing, BackgroundColour = CONFIG.Colour)

        Wrap the function automatically in an Async IO Task.
        """
        return self._LOOP.create_task(self.Call(func, *args, **kwargs))

    @__setattrs
    async def Call(self, func: Callable, *args, **kwargs) -> Any:
        """
        Call your earlier set synchronous function and submits it to the ThreadPoolExecutor.
        You can pass regular and keyword arguments in this method.

        example: SIA.Call(ImageGenerator, CONFIG.Sizing, BackgroundColour = CONFIG.Colour)

        Don't forget to await!
        """
        self._future: asyncio.Future = self._LOOP.run_in_executor(self._POOL, partial(func, **kwargs), *args)

        self._result = await self._future
        return self._result

    @property
    def result(self):
        """
        Returns None if the Thread has not yet finished.
        """
        return self._result

    @property
    def args(self) -> tuple:
        """
        Returns the latest passed args.
        """
        return self._ARGS or None

    @property
    def kwargs(self) -> dict:
        """
        Returns the latest passed kwargs.
        """
        return self._KWARGS or None