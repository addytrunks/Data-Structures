def reverseStringRecursive(string):
    if len(string) == 0:
        return string
    return  reverseStringRecursive(string[1:])+ string[0] 

# hello -> rev('ello') + 'h' -> rev('llo') + 'e' + 'h' -> rev('lo') + 'l' +'e' + 'h'
