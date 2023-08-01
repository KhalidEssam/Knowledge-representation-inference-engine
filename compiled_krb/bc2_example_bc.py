# bc2_example_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def Same_brand(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('Car', 'Brand_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.Same_brand: got unexpected plan from when clause 1"
            with engine.prove('Car', 'Brand_of', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.Same_brand: got unexpected plan from when clause 2"
                if context.lookup_data('car1') != context.lookup_data('car2') and context.lookup_data('Brand1') == context.lookup_data('Brand2'):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Same_Category(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('Car', 'Category_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.Same_Category: got unexpected plan from when clause 1"
            with engine.prove('Car', 'Category_of', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.Same_Category: got unexpected plan from when clause 2"
                if context.lookup_data('car1') != context.lookup_data('car2') and context.lookup_data('Category1') == context.lookup_data('Category2'):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Same_Country(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('Car', 'country_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.Same_Country: got unexpected plan from when clause 1"
            with engine.prove('Car', 'country_of', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.Same_Country: got unexpected plan from when clause 2"
                if context.lookup_data('car1') != context.lookup_data('car2') and context.lookup_data('Country1') == context.lookup_data('Country2'):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def select_Country(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'any_country', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.select_Country: got unexpected plan from when clause 1"
            with engine.prove('Car', 'country_of', context,
                              (rule.pattern(1),
                               rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc2_example.select_Country: got unexpected plan from when clause 2"
                with engine.prove('questions', 'any_category', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc2_example.select_Country: got unexpected plan from when clause 3"
                    with engine.prove('Car', 'Category_of', context,
                                      (rule.pattern(1),
                                       rule.pattern(2),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc2_example.select_Country: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'any_Brand', context,
                                          (rule.pattern(3),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc2_example.select_Country: got unexpected plan from when clause 5"
                            with engine.prove('Car', 'Brand_of', context,
                                              (rule.pattern(1),
                                               rule.pattern(3),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc2_example.select_Country: got unexpected plan from when clause 6"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def how_related(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'relation', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc2_example.how_related: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc2_example')
  
  bc_rule.bc_rule('Same_brand', This_rule_base, 'relation',
                  Same_brand, None,
                  (contexts.variable('car1'),
                   contexts.variable('car2'),
                   pattern.pattern_literal('Same_brand'),
                   contexts.variable('Brand2'),),
                  (),
                  (contexts.variable('car1'),
                   contexts.variable('Brand1'),
                   contexts.variable('car2'),
                   contexts.variable('Brand2'),))
  
  bc_rule.bc_rule('Same_Category', This_rule_base, 'relation',
                  Same_Category, None,
                  (contexts.variable('car1'),
                   contexts.variable('car2'),
                   pattern.pattern_literal('Same_Category'),
                   contexts.variable('Category1'),),
                  (),
                  (contexts.variable('car1'),
                   contexts.variable('Category1'),
                   contexts.variable('car2'),
                   contexts.variable('Category2'),))
  
  bc_rule.bc_rule('Same_Country', This_rule_base, 'relation',
                  Same_Country, None,
                  (contexts.variable('car1'),
                   contexts.variable('car2'),
                   pattern.pattern_literal('Same_Country'),
                   contexts.variable('Country2'),),
                  (),
                  (contexts.variable('car1'),
                   contexts.variable('Country1'),
                   contexts.variable('car2'),
                   contexts.variable('Country2'),))
  
  bc_rule.bc_rule('select_Country', This_rule_base, 'relation',
                  select_Country, None,
                  (contexts.variable('car1'),
                   contexts.variable('car2'),
                   contexts.variable('country'),
                   contexts.variable('select_Country'),),
                  (),
                  (contexts.variable('ans'),
                   contexts.variable('car1'),
                   contexts.variable('ans1'),
                   contexts.variable('ans2'),))
  
  bc_rule.bc_rule('how_related', This_rule_base, 'how_related',
                  how_related, None,
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   pattern.pattern_tuple((contexts.variable('p1_type'), contexts.variable('p2_type'),), None),),
                  (),
                  (contexts.variable('person1'),
                   contexts.variable('person2'),
                   contexts.variable('p1_type'),
                   contexts.variable('p2_type'),))


Krb_filename = '..\\bc2_example.krb'
Krb_lineno_map = (
    ((14, 18), (27, 27)),
    ((20, 26), (29, 29)),
    ((27, 33), (30, 30)),
    ((34, 34), (31, 31)),
    ((47, 51), (34, 34)),
    ((53, 59), (36, 36)),
    ((60, 66), (37, 37)),
    ((67, 67), (38, 38)),
    ((80, 84), (40, 40)),
    ((86, 92), (42, 42)),
    ((93, 99), (43, 43)),
    ((100, 100), (44, 44)),
    ((113, 117), (54, 54)),
    ((119, 124), (56, 56)),
    ((125, 131), (57, 57)),
    ((132, 137), (58, 58)),
    ((138, 144), (59, 59)),
    ((145, 150), (60, 60)),
    ((151, 157), (61, 61)),
    ((170, 174), (74, 74)),
    ((176, 184), (76, 76)),
)
