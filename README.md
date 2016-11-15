# Broadlink RM3 Mini

## Dependencies

 * [python-broadlink](https://github.com/mjg59/python-broadlink)

## Discovery

First, you need to discover your RM3 Mini. (we are assuming that you did connect it to your WiFi)

```
python2 ./discover.py
```

## Learning codes

```
python2 ./learn.py code_name 0
```

Where 0 is index of discovered id. (take a look at config.json)

Codes are saved to commands.json. 

## Sending codes

```
python2 ./send.py code_name 0
```

Where 0 is index of discovered id. (take a look at config.json)

