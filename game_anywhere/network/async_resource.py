from abc import ABC, abstractmethod


class AsyncResource(ABC):
    @abstractmethod
    def nt_interrupt(self): ...

    @abstractmethod
    async def nt_close(self): ...

    async def interrupt_and_close(self):
        self.nt_interrupt()
        await self.nt_close()
