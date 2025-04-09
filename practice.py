def in_autotests_we_trust(x, y):
    if x == y:
        print('Test passed')
    else:
        print('Test failed')

in_autotests_we_trust(1, True)

in_autotests_we_trust(0, False)