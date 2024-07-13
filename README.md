## simple-rofi-picker

simple-rofi-picker is a project designed to create quick and efficient menus for launching virtually anything. 
It leverages Rofi as the user interface and utilizes a JSON configuration file to define various options.
A Python script automates launching the picker and starting a process composed of a given base command and the selected option's value.

### dependencies
 - python3
 - [rofi](https://github.com/davatorium/rofi)

### json config
```json
{
    "name": "notifier",
    "base_command": "notify-send %1",
    "case_sensitive": true,
    "options": [
        {
            "label": "One [1]",
            "value": "one"
        },
        {
            "label": "Two [2]",
            "value": "two"
        },
        {
            "label": "Three [2]",
            "value": "three"
        }
    ]
}
```
### Plans for Next Iterations
 - multiple values per option
 - multiple pickers per config?
