## rofi simple picker

### dependencies
  python3
  [rofi](https://github.com/davatorium/rofi)

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

### next interation 

 - multiple values per option
 - multiple picker per config 
