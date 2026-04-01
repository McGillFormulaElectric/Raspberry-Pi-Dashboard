uart_data = {   # {class_name: value}
    "front_brake_bar":  0,
    "rear_brake_bar":   0,
    "speed_bar":        0,
    "throttle_bar":     0,
    "front_brake_text": 0,
    "rear_brake_text":  0,
    "speed_text":       0,
    "throttle_text":    0,
}

id = {   # {id: class_name}
    1: "front_brake_bar",
    2: "rear_brake_bar",
    3: "speed_bar",
    4: "throttle_bar",
    5: "front_brake_text",
    6: "rear_brake_text",
    7: "speed_text",
    8: "throttle_text",
}

pages = {   # {page_num: {class_name: type}} 
    1: {
        "front_brake_bar":  "bar", #k: object_name, v:widget_type
        "rear_brake_bar":   "bar",
        "speed_bar":        "bar",
        "throttle_bar":     "bar",
        "front_brake_text": "text",
        "rear_brake_text":  "text",
        "speed_text":       "text",
        "throttle_text":    "text",
    }
}