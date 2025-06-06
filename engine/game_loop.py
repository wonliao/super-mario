"""主遊戲迴圈模組。

負責驅動遊戲各個模組並處理更新與繪製流程。
"""

# TODO: 建立遊戲迴圈並整合輸入、更新與渲染流程

class GameLoop:
    def __init__(self, physics_engine):
        self.physics = physics_engine
        self.running = False

    def run(self):
        """開始遊戲主迴圈。"""
        self.running = True
        while self.running:
            # TODO: 處理輸入、更新與渲染
            break
