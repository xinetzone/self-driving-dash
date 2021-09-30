from dataclasses import dataclass, asdict
import asyncio

import toml
from tools.obstacle.simulate import ObstacleInfo, obstacle_simulate


async def USB(root_dir, loop):
    self = ObstacleInfo(**obstacle_simulate())
    D = asdict(self)
    now = loop.time()
    with open(f'{root_dir}/obstacle.toml', 'a+') as fp:
        toml.dump({str(now): D}, fp)
    await asyncio.sleep(1e-2)


async def info(root_dir):
    with open(f'{root_dir}/obstacle.toml') as fp:
        w = toml.load(fp)


async def usb_run(save_dir, loop):
    usb_task = asyncio.create_task(USB(save_dir, loop))
    print_task = asyncio.create_task(info(save_dir))
    await usb_task
    await print_task
