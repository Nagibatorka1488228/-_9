def sort_sentence(s):
    l = s.split(' ')
    l = [x.lower() for x in sorted(l, key=len)]
    l[0] = l[0].capitalize()
    s = ' '.join(l)
    return s

if __name__ == "__main__":
    assert sort_sentence('Keep calm and carry on') == 'On and keep calm carry'
    print('OK')
