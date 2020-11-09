def _is_ascii_string(s):
    try:
        s.decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def norm_unicode_to_ascii(s):
    if not s:
        return ''

    if _is_ascii_string(s):
        return s

    return s.decode('utf-8')