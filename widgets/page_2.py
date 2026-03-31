from PySide6.QtWidgets import QLabel


def _set_badge_state(badge: QLabel, enabled: bool) -> None:
    if enabled:
        badge.setText("On")
        badge.setStyleSheet(
            "background-color: rgba(76, 175, 80, 50);"
            "color: #6DDC7A; font-size: 11px; font-weight: bold;"
            "border-radius: 10px; padding: 2px 8px;"
        )
    else:
        badge.setText("Off")
        badge.setStyleSheet(
            "background-color: rgba(226, 75, 74, 40);"
            "color: #E24B4A; font-size: 11px; font-weight: bold;"
            "border-radius: 10px; padding: 2px 8px;"
        )


def pulse_light(window, charging_on: bool = False, balancing_on: bool = False):
    """Update the page 2 BMS status badges."""
    if not hasattr(window, "badgeCharging") or not hasattr(window, "badgeBalancing"):
        return

    _set_badge_state(window.badgeCharging, charging_on)
    _set_badge_state(window.badgeBalancing, balancing_on)
