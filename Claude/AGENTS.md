# AGENTS.md

All changes must be logged in `CHANGELOG.md`.

## Core Instruction

- Never edit code unless the user explicitly asks for code changes.
- Default to analysis, explanation, debugging, review, and recommendations unless the request clearly authorizes implementation.
- When reviewing code, treat the user as `person 1` from `work.md` if that file is present. If `work.md` is missing, do not invent its contents.

## Project Summary

This repository is a PySide6 telemetry dashboard for a Raspberry Pi / Formula Electric workflow.

- The main desktop entrypoint is `main.py`.
- The live dashboard logic is in `dashboard/`.
- The runtime UI is loaded from `untitled/mainwindow.ui` with `QUiLoader`.
- Raspberry Pi helper scripts live in `config_scripts/`.

## Source Of Truth

When working on the dashboard, treat these files as authoritative:

- `main.py`
- `dashboard/dashboard_class.py`
- `dashboard/dynamic_logic.py`
- `dashboard/signals_and_pages.py`
- `widgets/page_2.py`
- `images/image_loader.py`
- `untitled/mainwindow.ui`

These files exist but are not the main runtime source of truth:

- `untitled/mainwindow_ui.py`
- `main/mainwindow_ui.py`
- `main/ui_mainwindow.py`
- `untitled/main.py`
- `untitled/main.qml`
- `untitled/main.cpp`
- `untitled/mainwindow.cpp`

They appear to be Qt Creator generated files, experiments, or alternate artifacts. Do not assume the app uses them unless a task explicitly says so.

## How The App Runs

- `main.py` constructs `dashboard.dashboard_class.Dashboard` and calls `run()`.
- `Dashboard` loads `untitled/mainwindow.ui`.
- UART data is read in `Dashboard.uart_store()`.
- The UI refresh loop runs on a `QTimer` in `Dashboard.uart_update()`.
- Dynamic widgets are mapped in `dashboard/signals_and_pages.py`.

## UART Notes

The current codebase uses simple framed UART packets:

- Byte 1: `0xFF` start byte
- Byte 2: signal id
- Byte 3: value

Ports referenced in the repo:

- Windows dev: `COM4`
- Raspberry Pi: `/dev/serial0`
- Raspberry Pi alternate: `/dev/ttyAMA5`

If UART behavior changes, update the parser and the id-to-widget mapping together.

## UI Editing Rules

- Make layout and widget changes in `untitled/mainwindow.ui`.
- Do not hand-edit generated `*_ui.py` files unless the task is specifically about generated code.
- Keep every dynamic widget's Qt `objectName` in sync with `dashboard/signals_and_pages.py`.
- If you rename a widget in Qt Designer, update:
  - `uart_data`
  - `id`
  - `pages`
  - any helper logic that depends on the widget naming pattern

Important: the stacked widget pages are not guaranteed to be added in numeric order. Use the current page widget's `objectName` instead of assuming `currentIndex() + 1` matches `page_N`.

## Dynamic Widget Conventions

`dashboard/dynamic_logic.py` contains generic helpers for:

- resizing bars
- updating text labels
- future LED/table helpers

When adding new bar widgets:

- make sure the bar widget and its track widget follow a naming pattern the helper can resolve
- keep both widgets on the same page
- verify the `objectName` values in the `.ui` file, not just what Qt Creator displays visually

When adding text widgets:

- the mapped widget should be a `QLabel`
- the `objectName` must match the value used in `signals_and_pages.py`

## Repo Footguns

- `widgets/uart_logic.py` appears to be older experimental code. The main runtime path is `dashboard/dashboard_class.py`.
- `README.md` is more of a working design note than a finished setup guide.
- `untitled/requirements.txt` lists `PySide6`, but the code also imports `serial`, so `pyserial` is also required in practice.
- `__pycache__/`, `.pyc`, and Qt Creator cache folders are generated noise and should not be edited or committed.

## Useful Commands

Run the desktop app from the repo root:

```bash
python main.py
```

Manual UART listener:

```bash
python test/testUart.py
```

Pi launch helper:

```bash
bash config_scripts/run_app.sh
```

Pi serial read helper:

```bash
bash config_scripts/read_port.sh
```

## When Adding A New Telemetry Signal

1. Add or identify the target widget in `untitled/mainwindow.ui`.
2. Confirm its `objectName`.
3. Add the widget to `dashboard/signals_and_pages.py`.
4. Add the UART id mapping in `dashboard/signals_and_pages.py`.
5. Make sure `dashboard/dynamic_logic.py` supports that widget type.
6. Run the app and verify the visible page updates correctly.

## Recommended Workflow

- Inspect `untitled/mainwindow.ui` first for real widget names.
- Then inspect `dashboard/signals_and_pages.py`.
- Then inspect `dashboard/dashboard_class.py` and `dashboard/dynamic_logic.py`.
- Prefer small, synchronized changes across UI names and Python mappings.
- If a widget appears in Qt Creator but updates fail at runtime, suspect an `objectName` mismatch before suspecting Qt itself.

## Communication Rule

- When diagnosing issues, explain the issue before proposing or making code edits.
- If the user has not explicitly authorized edits, stop at explanation and recommendations.
