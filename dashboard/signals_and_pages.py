uart_data = {   # {object_name: value}
    # Match the actual objectName values in untitled/mainwindow.ui.
    # page_1
    "frontbrakebar":     0,
    "rearbrakebar":      0,
    "speedbar":          0,
    "throttlebar":       0,
    "front_brake_text":  0,
    "rear_brake_text":   0,
    "speed_text":        0,
    "throttle_text":     0,
    # page_2
    "valCurrent":        0,
    "valVoltage":        0,
    "valMinTemp":        0,
    "valMaxTemp":        0,
    "valMinVolt":        0,
    "valMaxVolt":        0,
    "badgeCharging":     0,
    "badgeBalancing":    0,
    "dotCharging":       0,
    "dotBalancing":      0,
}

id = {   # {uart_id: object_name}
    1: "frontbrakebar",
    2: "rearbrakebar",
    3: "speedbar",
    4: "throttlebar",
    5: "front_brake_text",
    6: "rear_brake_text",
    7: "speed_text",
    8: "throttle_text",
    # page_2
    9:  "valCurrent",
    10: "valVoltage",
    11: "valMinTemp",
    12: "valMaxTemp",
    13: "valMinVolt",
    14: "valMaxVolt",
    15: "badgeCharging",
    16: "badgeBalancing",
    17: "dotCharging",
    18: "dotBalancing",
}

pages = {   # {page_object_name: {object_name: widget_type}}
    "page_1": {
        "frontbrakebar":    "bar",
        "rearbrakebar":     "bar",
        "speedbar":         "bar",
        "throttlebar":      "bar",
        "front_brake_text": "text",
        "rear_brake_text":  "text",
        "speed_text":       "text",
        "throttle_text":    "text",
    },
    "page_2": {
        "valCurrent":     "text",
        "valVoltage":     "text",
        "valMinTemp":     "text",
        "valMaxTemp":     "text",
        "valMinVolt":     "text",
        "valMaxVolt":     "text",
        "badgeCharging":  "badge",
        "badgeBalancing": "badge",
        "dotCharging":    "led",
        "dotBalancing":   "led",
    },
}
