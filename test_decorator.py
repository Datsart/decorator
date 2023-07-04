def p_wrapper(func):
    print(1, func)

    def tag_wrapper(*args, **kwargs):
        print(2, 'arg', args)
        print(3, 'kwargs', kwargs)
        markup = func(*args, **kwargs)
        print(4, markup)
        return f'<p>{markup}</p>'

    return tag_wrapper


@p_wrapper
def render_input(field):
    return f'5 ---- <input id="id_{field}" type="text" name="{field}">'


username = render_input('username')
print(6, username)
