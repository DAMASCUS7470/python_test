def in_autotests_we_trust(x, y):
    if x == y:
        print('PASSED')
    else:
        print('FAILED')

in_autotests_we_trust('10', '10')

in_autotests_we_trust(0, False)
