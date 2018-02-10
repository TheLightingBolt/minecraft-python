import time
import serwPol

mc = serwPol.podlacz()

def dotykMidasa():
	gold = 41
	water = 9
	air = 0

	while True:
		pos = mc.player.getTilePos()
		x = pos.x
		blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
		if blockBelow != air and blockBelow != water:
   			mc.setBlock(pos.x, pos.y - 1, pos.z, gold)
		time.sleep(0.5)

dotykMidasa()
