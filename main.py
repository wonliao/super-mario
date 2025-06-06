"""Super Mario 遊戲入口點。

此檔案負責初始化各個模組並啟動遊戲。
"""

# TODO: 整合所有模組並啟動遊戲主迴圈

from engine.physics import PhysicsEngine
from engine.game_loop import GameLoop


def main():
    physics = PhysicsEngine()
    game = GameLoop(physics)
    game.run()


if __name__ == "__main__":
    main()
