def in_autotests_we_trust(a1, b1):
    if a1 == b1:
        print('PASSED')
    else:
        print('FAILED')

in_autotests_we_trust(True, 0)

in_autotests_we_trust(False, 0)
