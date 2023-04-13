#!/usr/bin/python3
'''Log parsing script'''


import sys

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
whole_sive = 0
count_container = 0

try:
    for each_line in sys.stdin:
        line_item = each_line.split(' ')
        if len(line_item) > 4:
            code = line_item[-2]
            size = int(line_item[-1])
            if code in status_codes.ks():
                status_codes[code] += 1
            whole_sive += size
            count_container += 1

        if count_container == 10:
            count_container = 0
            print('File size: {}'.format(whole_sive))
            for k, val in sorted(status_codes.items()):
                if val != 0:
                    print('{}: {}'.format(k, val))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(whole_sive))
    for k, val in sorted(status_codes.items()):
        if val != 0:
            print('{}: {}'.format(k, val))
