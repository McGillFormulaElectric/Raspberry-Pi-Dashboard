All changes must be logged in `CHANGELOG.md`.

---

## 2026-04-06 — page_2 widget mapping + page_1 name fix

### Context
`signals_and_pages.py` had no `page_2` entry. `dashboard/object_id.xlsx` had incorrect
objectNames for the four bar widgets on page_1 (`front_brake_bar` etc. instead of the
actual `.ui` names `frontbrakebar` etc.), and no page_2 data at all.

### Changes

#### `dashboard/signals_and_pages.py`
- Added 10 page_2 dynamic widgets to `uart_data` (IDs 9–18):
  `valCurrent`, `valVoltage`, `valMinTemp`, `valMaxTemp`, `valMinVolt`, `valMaxVolt`,
  `badgeCharging`, `badgeBalancing`, `dotCharging`, `dotBalancing`
- Added corresponding entries to `id` dict (keys 9–18)
- Added `"page_2"` block to `pages` dict with correct widget types
  (`text` for val* labels, `badge` for badge* labels, `led` for dot* labels)
- page_1 mappings unchanged (were already correct)

#### `dashboard/object_id.xlsx`
- **Sheet "Page 1 UI Elements"**: fixed four bar widget names that were wrong:
  - `front_brake_bar` → `frontbrakebar`
  - `rear_brake_bar`  → `rearbrakebar`
  - `speed_bar`       → `speedbar`
  - `throttle_bar`    → `throttlebar`
- **Sheet "Page 2 UI Elements"** (new): added 10 rows for page_2 dynamic widgets
  (IDs 9–18) matching the `.ui` objectNames exactly
- **Sheet "Python Dicts"**: rebuilt to reflect all of the above corrections for both
  `id`, `uart_data`, and `pages` dicts
