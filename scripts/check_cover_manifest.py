#!/usr/bin/env python3
"""Read-only geometry check using human-inspected bounds; needs Pillow."""
import json, sys
from pathlib import Path
from PIL import Image


def check(item, root):
    errors = []
    path = root / item['file']
    with Image.open(path) as img:
        if img.size != (1600, 1600): errors.append('canvas must be 1600x1600')
    x0,y0,x1,y1 = item['bbox']
    w,h = x1-x0,y1-y0
    if not (0 <= x0 < x1 <= 1600 and 0 <= y0 < y1 <= 1600):
        errors.append('invalid subject bounds')
    if abs((x0+x1)/2 - 800) > 3: errors.append('subject is not horizontally centred')
    preset = item['preset']
    if preset in ('bracelet','necklace'):
        target = 1000 if preset == 'bracelet' else 1200
        if w > target+3 or h > target+3 or abs(max(w,h)-target)>3:
            errors.append(f'subject must fit {target} square with longest side {target}')
        if abs((y0+y1)/2 - 800)>3: errors.append('circle is not vertically centred')
    elif preset in ('drop-earrings','stud-earrings','pendant'):
        expected = {'drop-earrings':(750,1200),'stud-earrings':(600,1000),'pendant':(None,1400)}[preset]
        if expected[0] and abs(w-expected[0])>3: errors.append('pair width differs from preset')
        bottom = item.get('pearl_bottom')
        if bottom is None or not y0 <= bottom <= y1 or abs(bottom-expected[1])>3:
            errors.append('pearl bottom absent, outside subject, or wrong margin')
        if preset == 'pendant' and (w>1203 or h>1203): errors.append('pendant exceeds 1200 square')
    else: errors.append('unknown preset')
    return {'file':item['file'], 'errors':errors}

if __name__ == '__main__':
    source = Path(sys.argv[1]).resolve()
    results = [check(i,source.parent) for i in json.loads(source.read_text())['covers']]
    print(json.dumps({'results':results,'note':'geometry only; supplied bounds require visual verification'},indent=2))
    sys.exit(1 if any(x['errors'] for x in results) else 0)
