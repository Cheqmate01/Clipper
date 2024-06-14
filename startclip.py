import sys
import clipboard
import json

defaultpath = './startclip.json'

def save_clip(data, filepath = defaultpath):
    with open(filepath, 'w') as f:
        json.dump(data, f)

def load_clip(key, filepath = defaultpath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            clipboard.copy(data[key])
    except:
        return {}

def list_clips(filepath = defaultpath):
    with open(filepath, 'r') as f:
        data = json.load(f)
        print(data)

if len(sys.argv) == 2:
    command = sys.argv[1]
    if command == 'save':
        key = input('What will you call this clip? ')
        clip = clipboard.paste()
        filepath = input('Define path to clip to. Enter to assume default ')
        if filepath == '':
            save_clip(data = {key: clip})
        else:
            save_clip(filepath = filepath, data = {key: clip})
        print('Clip has been saved. See ya.')
    elif command == 'load':
        key = input('What clip would you like to retrieve? ')
        filepath = input('Define path to load from. Enter to assume default ')
        if filepath == '':
            load_clip(key = key)
        else:
            load_clip(filepath = filepath, key = key)
        print('Clip has been loaded. Enjoy.')
    elif command == 'list':
        filepath = input('Define path to load from. Enter to assume default ')
        if filepath == '':
            list_clips()
        else:
            list_clips(filepath = filepath)
        pass
    else:
        print('Please enter correct command')
else:
    print('Please enter correct command')
