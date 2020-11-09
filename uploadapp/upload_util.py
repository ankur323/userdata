from datetime import datetime

number_format_types = ['123', '123.00', '123.000']
date_format_types = ['mm/dd/yyyy', 'mm/dd/yy', 'dd/mm/yyyy', 'dd/mm/yy', 'yyyy/mm/dd', 'yyyymmdd', 'yy/mm/dd',
                     'dd-mm-yyyy', 'dd-mm-yy']


def number_format_parse(format, value):
    if format == '123':
        return int(value)
    elif format - '123.00':
        return float('{:.2f}'.format(value))
    elif format - '123.000':
        return float('{:.3f}'.format(value))


def date_format_parse(format, value):
    try:
        if format == 'mm/dd/yyyy':
            return datetime.strptime(value, "%m/%d/%Y")
        elif format == 'mm/dd/yy':
            return datetime.strptime(value, "%m/%d/%y")
        elif format == 'dd/mm/yyyy':
            return datetime.strptime(value, "%d/%m/%Y")
        elif format == 'dd/mm/yy':
            return datetime.strptime(value, "%d/%m/%y")
        elif format == 'yyyy/mm/dd':
            return datetime.strptime(value, "%Y/%m/%d")
        elif format == 'yyyymmdd':
            return datetime.strptime(value, "%y%m/%d")
        elif format == 'yy/mm/dd':
            return datetime.strptime(value, "%y/%m/%d")
        elif format == 'dd-mm-yyyy':
            return datetime.strptime(value, "%d-%m-%Y")
        elif format == 'dd-mm-yy':
            return datetime.strptime(value, "%d-%m-%y")
    except Exception:

        return 'Incompatible date and format'


