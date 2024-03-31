import settings
import obstacle

class Coin(obstacle.Obstacle):
  def __init__(self):
    super().__init__(20, 1, "coin.png", settings.SPEED)
