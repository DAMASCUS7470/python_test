def in_autotests_we_trust(p, q):
    if p == q:
        print('Test passed')
    else:
        print('Test failed')

in_autotests_we_trust(1, 1)

in_autotests_we_trust(False, 0)