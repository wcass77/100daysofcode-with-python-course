from itertools import cycle
import time

LIGHTS = ["Green", "Yellow", "Red"]
CHANGE_TIME = 2  # seconds
SLEEP_TIME = 0.005


class TrafficLight:
    _change_time = CHANGE_TIME

    def __init__(self):
        self._light = cycle(LIGHTS)
        self._color = next(self._light)
        self._last_change = time.time()

    @property
    def color(self):
        time_delta = time.time() - self._last_change
        if time_delta >= self._change_time:
            n = int(time_delta // self._change_time)
            for _ in range(n):
                self._color = next(self._light)
            self._last_change = time.time()
        return self._color

    def wait_for_light_change(self):
        start_color = self._color
        while start_color == self.color:
            time.sleep(SLEEP_TIME)
        return self.color


if __name__ == "__main__":
    light = TrafficLight()
    print("You are stuck in traffic at a light")
    try:
        while True:
            print(f"The traffic light is {light.color}")
            light.wait_for_light_change()
    except KeyboardInterrupt as e:
        print("You decide to get out of your car and ride a bike")

