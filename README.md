# Macro Runner

A Python script to execute Hammerspoon-style Lua macros on macOS with customizable timing and looping. Loads macros from the `lua/` subfolder, supporting mouse movements, clicks, and key strokes (single or with modifiers like `cmd`, `shift`).

## Features
- **Dynamic Lua Loading**: Runs `.lua` files from `lua/` (e.g., `lua/mymacro.lua`).
- **Command Support**: Executes `hs.mouse.setAbsolutePosition`, `hs.eventtap.leftClick`, and `hs.eventtap.keyStroke`.
- **Random Timing**: Applies random step intervals (0.45-0.82s) between commands and sleep (0.5-5.0s) between loops.
- **Status Display**:
  - Simple: `- 1/3, Sleep:1.80s`
  - Detailed: `- 1/3, +0.45, +0.71, ..., Sleep:1.80s` (with `detail` flag).
- **Command-Line Interface**:
  - `python run.py <luaname>`: Simple mode.
  - `python run.py <luaname> detail`: Detailed mode.

## Requirements
- Python 3.10+
- `pyautogui` (`pip3 install pyautogui`)
- macOS accessibility permissions

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/horazip/macro-runner.git
   cd macro-runner

---

# 宏運行器 (Macro Runner)

一個在 macOS 上執行 Hammerspoon 風格 Lua 宏的 Python 腳本，支援自訂隨機時間間隔和循環。從 `lua/` 子資料夾載入宏，支援滑鼠移動、點擊和按鍵（單鍵或帶修飾鍵如 `cmd`、`shift`）。

## 功能
- **動態 Lua 載入**：從 `lua/` 載入 `.lua` 文件（例如 `lua/mymacro.lua`）。
- **支援指令**：執行 `hs.mouse.setAbsolutePosition`、`hs.eventtap.leftClick` 和 `hs.eventtap.keyStroke`。
- **隨機時間**：
  - 指令間隨機間隔：0.45-0.82 秒。
  - 循環間隨機睡眠：0.5-5.0 秒。
- **狀態顯示**：
  - 簡單模式：`- 1/3, Sleep:1.80s`
  - 詳細模式（帶 `detail` 參數）：`- 1/3, +0.45, +0.71, ..., Sleep:1.80s`
- **命令列介面**：
  - `python run.py <luaname>`：簡單模式。
  - `python run.py <luaname> detail`：詳細模式。

## 需求
- Python 3.10 或以上版本
- `pyautogui`（安裝：`pip3 install pyautogui`）
- macOS 存取權限

## 安裝
1. 複製專案：
   ```bash
   git clone https://github.com/horazip/macro-runner.git
   cd macro-runner
