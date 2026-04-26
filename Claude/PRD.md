# Raspberry Pi Dashboard PRD

All changes must be logged in `CHANGELOG.md`.

## 1. Document Overview

### Product Name
Raspberry Pi Dashboard

### Document Purpose
Define the product requirements for a PySide6-based telemetry dashboard that runs on a Raspberry Pi and displays live vehicle telemetry received over UART.

### Status
Working PRD based on the current repository implementation and existing design notes in `README.md` and `CLAUDE.md`.

## 2. Product Summary

The Raspberry Pi Dashboard is an in-car or bench-top telemetry display for a Formula Electric workflow. It loads a Qt Designer UI, listens for framed UART packets, stores the latest values for known signal IDs, and updates on-screen telemetry widgets in near real time.

The current product already supports a fullscreen desktop-style dashboard with page navigation, four live bar indicators, and four live text readouts. The intended next phase is to generalize the update pipeline so additional widget types, additional pages, stale-data handling, and more robust UART data storage can be added cleanly.

## 3. Problem Statement

The team needs a lightweight dashboard that can run directly on Raspberry Pi hardware, consume low-latency telemetry from embedded systems, and display the most important vehicle values clearly during development and testing.

Today, telemetry handling is functional but still narrow in scope:

- The live path is centered on a single main page.
- UART parsing is simple and assumes fixed 3-byte frames.
- UI updates currently support bars and text only.
- Data freshness, locking, and page-specific extensibility are only partially implemented or planned.

The product should evolve into a reliable, modular telemetry UI that remains responsive under continuous UART updates and is easy for the team to extend as more signals and pages are added.

## 4. Goals

### Primary Goals

- Display key telemetry values in real time on Raspberry Pi hardware.
- Provide an at-a-glance dashboard UI suitable for vehicle testing and bench validation.
- Keep the runtime architecture simple enough for students to extend safely.
- Support page-based dashboards so only visible UI elements are updated.

### Secondary Goals

- Support future widget types such as LEDs, tables, and page-specific status badges.
- Detect stale telemetry and visually indicate data loss.
- Separate UART reading, parsing, storage, and UI rendering responsibilities more cleanly.

## 5. Non-Goals

- Cloud telemetry storage or remote dashboards.
- Historical charting or analytics.
- Multi-user authentication or permissions.
- Complex deployment orchestration beyond local/Pi startup scripts.
- High-bandwidth binary protocols beyond the current lightweight UART frame format.

## 6. Users

### Primary Users

- Formula Electric team members monitoring live vehicle signals.
- Developers validating embedded-to-dashboard signal flow.
- Test operators using the Raspberry Pi dashboard during setup and debugging.

### User Needs

- Fast startup and fullscreen readability.
- Immediate confirmation that telemetry is being received.
- Simple page navigation.
- Clear visual distinction between healthy data and stale or missing data.

## 7. Current Product Scope

The repository currently implements the following:

- PySide6 application entrypoint in `main.py`.
- UI loaded dynamically from `untitled/mainwindow.ui`.
- Fullscreen dashboard window with hidden cursor.
- UART serial connection using `pyserial`.
- Framed UART input with the format `0xFF`, `signal_id`, `value`.
- In-memory mapping from signal IDs to widget object names.
- A timer-driven update loop running every 5 ms.
- A main telemetry page (`page_1`) with:
  - 4 dynamic bars:
    - `frontbrakebar`
    - `rearbrakebar`
    - `speedbar`
    - `throttlebar`
  - 4 dynamic text labels:
    - `front_brake_text`
    - `rear_brake_text`
    - `speed_text`
    - `throttle_text`
- Keyboard shortcuts for page navigation, fullscreen toggle, minimize, and quit.

The repository also contains early or partial support for:

- `page_2` BMS-style status badges (`badgeCharging`, `badgeBalancing`)
- Generic dynamic UI helper functions for future LED/table support
- Raspberry Pi helper scripts in `config_scripts/`

## 8. Target Product Vision

The dashboard should become a modular telemetry platform where:

- UART data ingestion is decoupled from UI rendering.
- Signal IDs are centrally defined.
- Each page declares which widgets it owns.
- Only the active page is refreshed.
- New widget types can be added through generic helpers instead of page-specific logic.
- Missing or stale data is clearly indicated without crashing or freezing the UI.

## 9. Functional Requirements

### FR1. Application Startup

- The app shall launch from `main.py`.
- The app shall load the Qt UI from `untitled/mainwindow.ui`.
- The app shall open in fullscreen mode by default.
- The app shall hide the mouse cursor during runtime.

### FR2. UART Connectivity

- The app shall connect to a configured serial port on supported hardware.
- The app shall support the current UART packet structure:
  - byte 1: start byte `0xFF`
  - byte 2: signal ID
  - byte 3: value
- The app shall ignore malformed frames until the next valid start byte is found.
- The app shall fail gracefully if the serial port is unavailable.

### FR3. Signal Storage

- The app shall store the latest known value for each recognized signal.
- Each signal ID shall map to a named UI element or logical signal target.
- The next iteration should store both value and timestamp for each signal.
- The next iteration should protect shared UART data access if reading and writing occur from separate execution contexts.

### FR4. Page-Aware Rendering

- The app shall detect the currently visible stacked-widget page.
- The app shall update only widgets assigned to that page.
- The app shall use page metadata to determine each widget's update behavior.

### FR5. Dynamic Widget Updates

- The app shall support bar updates based on percentage-like values.
- The app shall support text label updates for numeric or string values.
- The next iteration should support LED-style indicators.
- The next iteration should support table-cell updates.
- The next iteration should support BMS status badge updates on `page_2`.

### FR6. Navigation and Operator Controls

- The app shall allow moving between pages with keyboard shortcuts.
- The app shall allow toggling fullscreen mode.
- The app shall allow minimizing the application.
- The app shall allow quitting via keyboard shortcut.

### FR7. Data Freshness

- The next iteration should track timestamps for incoming signal values.
- If no new data is received for more than 2 seconds, applicable widgets should show a stale-data state.
- Bars and tables are the highest-priority stale-data candidates based on current design notes.
- Stale-data presentation should default to a greyed-out or visually muted state.

## 10. Non-Functional Requirements

### Performance

- The UI should feel responsive under continuous UART traffic.
- Telemetry refresh should happen fast enough to appear real time to operators.
- Page transitions should remain smooth while the update loop is active.

### Reliability

- Serial failures should not hard-crash the application.
- Unknown UART IDs should be ignored safely with debuggable logging.
- Widget lookups should fail safely when a named widget is missing.

### Maintainability

- Widget object names in the `.ui` file must remain synchronized with Python mappings.
- Dynamic widget behavior should be implemented through reusable helpers.
- Signal definitions and page mappings should remain centralized.

### Portability

- The dashboard should support Raspberry Pi runtime ports such as `/dev/serial0` or `/dev/ttyAMA5`.
- Development workflows should remain possible on Windows using ports such as `COM4`.

## 11. UX Requirements

- The main dashboard shall prioritize readability over dense detail.
- Telemetry bars shall visually communicate magnitude quickly.
- Text values shall be legible at a glance.
- The fullscreen layout shall suit touchscreen or kiosk-like deployment.
- Operators shall be able to tell when a page has no live data or stale data.

## 12. Technical Constraints

- Frontend/runtime stack: Python + PySide6
- Serial communication: `pyserial`
- UI source of truth: `untitled/mainwindow.ui`
- Current runtime architecture: `dashboard/dashboard_class.py`, `dashboard/dynamic_logic.py`, `dashboard/signals_and_pages.py`
- Current protocol assumption: 3-byte UART frames with 1-byte values
- Current design is tightly coupled to Qt `objectName` values

## 13. Risks

- `objectName` mismatches between the `.ui` file and Python mappings can silently break updates.
- The current UART storage model only keeps raw values, not timestamps or validity metadata.
- If UART reading and UI rendering move to separate threads, unsynchronized shared state may introduce race conditions.
- Hardcoded port selection may cause deployment friction across environments.
- Placeholder helper methods may create false confidence unless clearly marked as not yet integrated.

## 14. Milestones

### Milestone 1: Baseline Dashboard

- Load UI successfully
- Connect to UART
- Render live bars and text on `page_1`
- Support fullscreen operation and page navigation

### Milestone 2: Modular Signal Pipeline

- Separate UART reader, parser, and store responsibilities
- Centralize signal IDs and page mappings
- Support timestamped values in shared storage

### Milestone 3: Robust Multi-Page Rendering

- Refresh only visible page widgets
- Add generic LED and table update helpers
- Integrate `page_2` status widgets into the live update path

### Milestone 4: Reliability and Stale-Data UX

- Detect data loss after 2 seconds
- Grey out stale widgets
- Add thread-safe access to shared UART data if concurrency is introduced

## 15. Acceptance Criteria

The product will be considered successful for the next phase when:

- The dashboard launches reliably on target hardware.
- Known UART frames update the correct widgets on the correct page.
- The visible page updates without obvious lag.
- Unknown or malformed UART frames do not crash the app.
- The architecture is clear enough that new telemetry signals can be added with predictable changes.
- Planned stale-data behavior and multi-widget extensibility have a clear implementation path.

## 16. Open Questions

- Should telemetry values remain 1-byte only, or will larger payloads be needed soon?
- Should the serial port be configurable at runtime instead of hardcoded?
- Should `page_2` BMS widgets be driven by the same ID map or by separate higher-level state?
- Which signals are mission-critical enough to require stale-data indicators first?
- Should the refresh timer remain at 5 ms, or be relaxed to reduce unnecessary work?

## 17. Recommended Next Step

The immediate product step should be to formalize the telemetry data model so each signal stores `value`, `timestamp`, and widget/page metadata. That change unlocks stale-data handling, safer page-specific updates, and cleaner support for future widget types without rewriting the dashboard loop repeatedly.
