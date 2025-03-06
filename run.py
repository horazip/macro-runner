import pyautogui
import time
import random
import sys
import os

# Helper class to mimic hs.geometry.point(x, y)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Simulated hs.mouse namespace
class Mouse:
    @staticmethod
    def setAbsolutePosition(point):
        pyautogui.moveTo(point.x, point.y, duration=0.1)

    @staticmethod
    def getAbsolutePosition():
        x, y = pyautogui.position()
        return Point(x, y)

# Simulated hs.eventtap namespace
class EventTap:
    @staticmethod
    def leftClick(point):
        pyautogui.click(x=point.x, y=point.y, button="left")

    @staticmethod
    def keyStroke(modifiers, key):
        modifier_map = {
            "cmd": "command", "shift": "shift", "ctrl": "ctrl", "alt": "option"
        }
        for mod in modifiers:
            pyautogui.keyDown(modifier_map.get(mod, mod))
        if key:  # Only press key if non-empty
            pyautogui.press(key)
        for mod in reversed(modifiers):
            pyautogui.keyUp(modifier_map.get(mod, mod))

# Function to parse and execute Hammerspoon-like commands from Lua
def execute_command(cmd):
    cmd = cmd.strip()
    if not cmd or cmd.startswith("--"):  # Skip empty lines or comments
        return None
    if cmd.startswith("hs.mouse.setAbsolutePosition(hs.geometry.point("):
        x = int(cmd.split("(")[2].split(",")[0])
        y = int(cmd.split(",")[1].split(")")[0])
        Mouse.setAbsolutePosition(Point(x, y))
    elif cmd == "hs.eventtap.leftClick(hs.mouse.getAbsolutePosition())":
        EventTap.leftClick(Mouse.getAbsolutePosition())
    elif cmd.startswith("hs.eventtap.keyStroke("):
        parts = cmd.split("hs.eventtap.keyStroke(")[1].rstrip(")")
        modifiers_str, key = parts.split("}, \"") if "}, \"" in parts else (parts.split(", \"")[0], parts.split(", \"")[1].rstrip("\""))
        modifiers = modifiers_str.strip("{").strip("}").split(", ") if modifiers_str.strip("{}") else []
        modifiers = [m.strip("\"") for m in modifiers]
        key = key.strip("\"")
        EventTap.keyStroke(modifiers, key)
    return cmd

# Function to load and execute macro from a .lua file
def play_macro(lua_file):
    with open(lua_file, "r") as f:
        lines = f.readlines()
    
    start_time = time.time()
    cumulative_time = 0.0
    step_intervals = []
    
    for i, line in enumerate(lines):
        cmd = execute_command(line)
        if cmd is None:
            continue
        if i > 0:
            step_interval = random.uniform(min_step_interval, max_step_interval)
            step_intervals.append(step_interval)
            cumulative_time += step_interval
            elapsed = time.time() - start_time
            if elapsed < cumulative_time:
                time.sleep(cumulative_time - elapsed)
    
    return step_intervals

# Configuration
min_step_interval = 0.45
max_step_interval = 0.82
loop_count = 3
min_sleep = 0.5
max_sleep = 5.0

# Parse command-line arguments
if len(sys.argv) < 2:
    print("Error: Please provide a Lua filename (e.g., 'python run.py luaname')")
    sys.exit(1)

lua_name = sys.argv[1]  # First argument: Lua filename
lua_file = os.path.join("lua", f"{lua_name}.lua")  # Path: lua/luaname.lua
show_details = len(sys.argv) > 2 and sys.argv[2] == "detail"  # Second argument: detail (optional)

# Check if the Lua file exists
if not os.path.isfile(lua_file):
    print(f"Error: File '{lua_file}' not found in 'lua/' subfolder")
    sys.exit(1)

# Run the macro in a loop with conditional status display
for i in range(loop_count):
    status = f"- {i + 1}/{loop_count}"
    step_intervals = play_macro(lua_file)
    
    if show_details:
        intervals_str = ", ".join([f"+{interval:.2f}" for interval in step_intervals])
        if i < loop_count - 1:
            sleep_time = random.uniform(min_sleep, max_sleep)
            print(f"{status}, {intervals_str}, Sleep:{sleep_time:.2f}s")
            time.sleep(sleep_time)
        else:
            print(f"{status}, {intervals_str}, Completed")
    else:
        if i < loop_count - 1:
            sleep_time = random.uniform(min_sleep, max_sleep)
            print(f"{status}, Sleep:{sleep_time:.2f}s")
            time.sleep(sleep_time)
        else:
            print(f"{status}, Completed")