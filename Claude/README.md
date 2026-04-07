All changes must be logged in `CHANGELOG.md`.

-separate uart logic and dynamic logic
-create uart_store in uart logic folder and uart_update method in dashbaord

dynamic logic:
-general bar resize method (window, class_name, value)
-general led blink method (window, class_name, bool)
-general table fill method (window, class_name, value)
-general text write method

uart store:
-read byte, parse_byte, store_byte
-make a dictionary that stores latest uart values
-make an id system for all data, (id, value) in a spreadsheet
-constantly updating in real time
-for the tables each r,c will have their own id
ex: page_map = {
    "main": {
        "bars": [(1, "speedBar"), (2, "rpmBar")],
        "leds": [(3, "faultLed")],
        "tables": [],
        "text": [(4, "gearLabel")]
    }
}

uart_update:
- only update the features that are on the same page. make a list for each page. list should divide between bars, led, tables, and text to allow for general methods to be called
- use if/else staments that read directly from the dictionary and not directly from the port

dashboard_class:
-uart_update every 20ms using qtimer
-add self.current_page

data loss:
-if no data for more than 2 seconds, turn grey. only applicable for bars and tables
-use a timestamp for each bars, table and text
-for each signal on current page:
    look it up in dictionary
    check timestamp, current_time - timestamp > 2
    update UI accordingly



thread locking:
-uart is writing and reading from a dictionary, possibly at the same time
-1 write thread and one read thread
-use thread locking

final project structure:
project/
    main.py
    dashboard/
        dashboard_class.py <-- self.uart_update()
        dynamic_logic.py 
    uart_logic/
        uart_reader.py
        uart_parser.py
        uart_store.py
    config/
        signal_ids.py
        page_map.py <-- maps pages to its dynamic elements
    tests/
        testUart.py
    bootup/
	    pi_config.sh
	    run_app.sh
	    read_port.sh
	

flowchart:
┌──────────────────────┐
│   UART data arrives  │
└──────────┬───────────┘
           │
           v
┌──────────────────────┐
│  uart_reader.py      │
│  read incoming bytes │
└──────────┬───────────┘
           │
           v
┌──────────────────────┐
│  uart_parser.py      │
│  parse into (id,val) │
└──────────┬───────────┘
           │
           v
┌──────────────────────────────┐
│  uart_store.py               │
│  store in shared dictionary  │
│  uart_data[id] = {           │
│      value, timestamp        │
│  }                           │
└──────────┬───────────────────┘
           │
           │   shared memory
           v
┌──────────────────────────────┐
│ dashboard_class.py           │
│ QTimer calls uart_update()   │
│ every 20 ms                  │
└──────────┬───────────────────┘
           │
           v
┌──────────────────────────────┐
│  check self.current_page     │
│  load page config from       │
│  page_map.py                 │
└──────────┬───────────────────┘
           │
           v
┌──────────────────────────────┐
│ for each signal on page:     │
│ - read value from dict       │
│ - check timestamp            │
│ - determine if stale         │
└──────────┬───────────────────┘
           │
   ┌───────┴────────┐
   │                │
   v                v
┌──────────────┐  ┌─────────────────┐
│ data is fresh│  │ data is stale   │
└──────┬───────┘  └────────┬────────┘
       │                   │
       v                   v
┌──────────────────────┐  ┌──────────────────────┐
│ call general UI      │  │ grey out widget      │
│ method based on type │  │ if applicable        │
│ - resize_bar         │  │                      │
│ - toggle_led          │  │                      │
│ - fill_table         │  │                      │
│ - write_text         │  │                      │
└──────────┬───────────┘  └──────────┬───────────┘
           │                         │
           └─────────────┬───────────┘
                         │
                         v
              ┌──────────────────────┐
              │ visible page updates │
              │ on dashboard         │
              └──────────────────────┘
