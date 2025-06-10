class PhysicsEngine:
    """簡易物理引擎範例"""

    def __init__(self):
        self.gravity = 9.8

    def apply_gravity(self, velocity: float) -> float:
        """套用重力於速度"""
        return velocity + self.gravity
