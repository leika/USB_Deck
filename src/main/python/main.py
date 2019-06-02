import iotframe
import uasyncio as asyncio
import machine


app = iotframe.IOTApplication("main")
eventLoop = app.prepareStart()


async def dbgSwitch():
    p0 = machine.Pin(0)
    await asyncio.sleep(1)
    while p0.value() == 1:
        await asyncio.sleep_ms(500)
    p2 = machine.Pin(2, machine.Pin.OUT)
    p2.value(0)

eventLoop.run_until_complete(dbgSwitch())
