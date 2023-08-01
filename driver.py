
import types
from pyke import contexts, pattern
import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal

# Compile and load .krb files in same directory that I'm in (recursively).
engine = knowledge_engine.engine(__file__)

fc_goal = goal.compile('Car.how_related($filter1, $filter2, $relationship)')


def fc_test(filter1=None, filter2=None):

    print(filter1)
    print(filter2)
    '''
        This function runs the forward-chaining example (fc_example.krb).
    '''
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    # Runs all applicable forward-chaining rules.
    engine.activate('fc_example')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    args = {}
    if filter1:
        filter1 = filter1.lower()
        args['filter1'] = filter1
    if filter2:
        args['filter2'] = filter2

    # print("doing proof")
    with fc_goal.prove(engine, **args) as gen:
        for vars, plan in gen:
            print("%s, %s are %s" %
                  (filter1, vars['filter2'], vars['relationship']))
    prove_time = time.time() - fc_end_time
    print()
    print("done")
    # engine.print_stats()
    print("fc time %.2f, %.0f asserts/sec" %
          (fc_time, engine.get_kb('Car').get_stats()[2] / fc_time))


def general(filter1=None, filter2='None', relationship=('None', 'None')):

    engine.reset()      # Allows us to run tests multiple times.
    # filter1 = filter1.lower()
    start_time = time.time()
    engine.activate('bc2_example')      # same rule base as bc2_test()
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    # print("doing proof")
    args = {}
    if filter1:
        args['filter1'] = filter1
    if filter2:
        args['filter2'] = filter2
    if relationship:
        args['relationship'] = relationship
    try:
        with engine.prove_goal(
            'bc2_example.how_related($filter1, $filter2, $relationship)',
            **args
        ) as gen:
            print("Here are some options based on your selections")
            for vars, plan in gen:
                print("%s " % (vars['filter1']))
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print()
    print("done")
    # engine.print_stats()
    # print(engine.)
    if prove_time > 0:
        print("bc time %.2f, %.0f goals/sec" %
              (prove_time,
               engine.get_kb('bc2_example').num_prove_calls / prove_time))


def bc2_test(filter1=None, filter2=None):
    engine.reset()      # Allows us to run tests multiple times.
    filter1 = filter1.lower()
    start_time = time.time()
    engine.activate('bc2_example')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    # print("doing proof")
    try:
        with engine.prove_goal(
            'bc2_example.how_related($filter1, $filter2, $relationship)',
            filter1=filter1) \
                as gen:
            for vars, plan in gen:
                print("%s, %s are %s" %
                      (filter1, vars['filter2'], vars['relationship']))
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print()
    print("done")
    # engine.print_stats()
    print("bc time %.2f, %.0f goals/sec" %
          (prove_time,
           engine.get_kb('bc2_example').num_prove_calls / prove_time))


# Need some extra goodies for general()...
