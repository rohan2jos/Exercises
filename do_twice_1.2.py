def print_spam(str_to_print):
    print str_to_print

def do_twice(f, str_arg):
    f(str_arg)
    f(str_arg)

do_twice(print_spam, "spam")

