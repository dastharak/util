# test_misc.py
# TEST : pytest -vs
import time
from util import spinner

def test_spinner():
    t = 1

    print(f"Test {t}: Simulated long task")
    print("Processing...", end="", flush=True)
    s = spinner()
    for _ in range(80):
        s.printtp()
        time.sleep(0.05)
    print("\bDone!")

    t+=1
    print(f"\nTest {t}: Reusable progress function")
    def show_progress(duration=4, message="Working"):
        print(f"{message}... ", end="", flush=True)
        s = spinner()
        steps = int(duration / 0.1)
        for _ in range(steps):
            s.printtp()
            time.sleep(0.05)
        print("\bDone!")

    show_progress(2, "Loading data")
    show_progress(4, "Training model")
    show_progress(3, "Saving file")

test_spinner()