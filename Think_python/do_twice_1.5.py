def print_twice(str_to_print):
    print str_to_print
    print str_to_print

def do_twice(f, str_arg):
    f(str_arg)
    f(str_arg)

def do_four(f, str_arg):
    do_twice(print_twice, str_arg)
    do_twice(print_twice, str_arg)

do_four(do_twice, "spam")
