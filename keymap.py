import json


keymap=json.load("keymap.json")
def save():
  json.dump("keymap.json",keymap)


