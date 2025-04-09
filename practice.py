def in_autotests_we_trust(a1, b1):
    if a1 == b1:
        print('Test passed')
    else:
        print('Test failed')

in_autotests_we_trust(True, 0)

in_autotests_we_trust(False, 0)