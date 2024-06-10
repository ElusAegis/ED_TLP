# Benchmark the performance of two different implementations of the same algorithm
import functools

# Using SageMath 9.0

import time
from gmpy2 import gmpy2
from sage.all import *

REPEAT = 1
NUMBER = 1

# def timer(f, *args):
#     return timeit.Timer(functools.partial(f, *args)).repeat(
#         repeat=REPEAT,
#         number=NUMBER
#     )

def now():
    return time.perf_counter_ns()


INTERVAL = 10
MILI_TO_S = 10 ** 9
INTERVAL_NS = INTERVAL * MILI_TO_S


def count_squarings_in_fixed_time():
    pass
    # TODO - Throw an error saying that this benchmark is not correct for the current implementation


def time_fixed_squarings(squarings):

    n = 6229205250449008408488810372435917442525505743598603566286880180064596734952053099221673849147518748692399578515831628412259027551369804282958904058809630420264031318325689626489250260020546212671383371411496565970115779226866501484729684350420421387107574180358960901752985144624550632252158672377981406168119986502705837004760655589162121670420147891606761984406546807870016164278720930862084677050553472632350920774838421622484403139811587663843084714602900714142650839197152586147630427406796612595096204464380274595090350217936191025805017452851931370665127804116777356024822439098514655521996611422252932038961
    r = 1743724424099666811431147607616692728826896443514242207251022167360334231794188502189239727905681649520198367880849093018870101376967446659325924877661130735527461957163130540894138745900941923700245232830214433940492810834306971987060530021931099050876151469281045398509726082192914920014136006891577804647901082138191447261475413873009694783720641377347310893325563523104910130150196172994236840850382206150539461295079402510124994605171161856343241143526252650336130173751940408292960684250460120602910899431931616599866508397641635456344269448841436759323323914976248980825239042395258981917924022550563782923632

    start = now()
    for _ in range(squarings):
        r = (r ** 2) % n
    stop = now()
    seconds = (stop - start) / MILI_TO_S
    print("Time taken naive:", seconds)
    print("Squaring rate naive:", squarings / seconds)

    start = now()
    for _ in range(squarings):
        r = gmpy2.powmod(r, 2, n)
    stop = now()
    seconds = (stop - start) / MILI_TO_S
    print("Time taken GMPY:", seconds)
    print("Squaring rate GMPY:", squarings / seconds)

    # We use the same parameters as in the other implementation
    Zn = IntegerModRing(n)
    r = Zn(r)

    start = now()
    for _ in range(squarings):
        power(r, 2)
    stop = now()
    seconds = (stop - start) / MILI_TO_S
    print("Time taken for Sage:", seconds)
    print("Squaring rate Sage:", squarings / seconds)


if __name__ == '__main__':
    # print(timer(count_squarings_in_fixed_time))

    test_amount = 10_000_000

    time_fixed_squarings(test_amount)
