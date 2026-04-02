uart_data = {   # {object_name: value}
    # Match the actual objectName values in untitled/mainwindow.ui.
    "frontbrakebar":     0,
    "rearbrakebar":      0,
    "speedbar":          0,
    "throttlebar":       0,
    "front_brake_text":  0,
    "rear_brake_text":   0,
    "speed_text":        0,
    "throttle_text":     0,
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
    }
}
