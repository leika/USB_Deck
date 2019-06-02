import ulogging
import uasyncio as asyncio
from micropython import const
import machine

g_AppLogger = ulogging.getLogger("iotMain")

IOT_STATE_INIT = const(0)
IOT_STATE_BOOTING = const(1)
IOT_STATE_RUNNING = const(2)
IOT_STATE_ADOPTING = const(3)


class IOTApplication:
    _status = IOT_STATE_INIT

    def __init__(self, name):
        g_AppLogger.info("Application Bootstrap !")
        self._status = IOT_STATE_INIT

    # Basic house keeping
    async def gcCleanupTask(self):
        while True:
            print("---")
            await asyncio.sleep(1)

    async def statusMessageTask(self):
        while True:
            print("--- status ---")
            self._status = self._status+1
            await asyncio.sleep(10)

    async def statusLedTask(self):
        statusPin = machine.PWM(machine.Pin(2))
        statusPin.duty(0)
        while True:
            if (self._status == IOT_STATE_INIT):
                statusPin.duty(0)
                await asyncio.sleep_ms(200)
            elif (self._status == IOT_STATE_BOOTING):
                statusPin.duty(512)
                await asyncio.sleep_ms(200)
                statusPin.duty(128)
                await asyncio.sleep_ms(200)
            elif (self._status == IOT_STATE_RUNNING):
                statusPin.duty(512)
                await asyncio.sleep_ms(500)
            elif (self._status == IOT_STATE_ADOPTING):
                statusPin.duty(512)
                await asyncio.sleep_ms(100)
                statusPin.duty(128)
                await asyncio.sleep_ms(100)
            else:
                await asyncio.sleep_ms(100)

    # Lifecycle

    def prepareStart(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.gcCleanupTask())
        loop.create_task(self.statusMessageTask())
        loop.create_task(self.statusLedTask())

        # Add more tasks and hookups for tasks
        return loop
