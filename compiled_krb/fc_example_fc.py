# fc_example_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def Same_category(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('Car', 'Category_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('Car', 'Category_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('car1') != context.lookup_data('car2') and context.lookup_data('Category1') == context.lookup_data('Category2') and context.lookup_data('Category1') not in (1,2,3,4,5,6,7,8,9):
              engine.assert_('Car', 'siblings',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),
                              rule.pattern(3).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def Select_Category(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('Car', 'Category_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('Car', 'siblings',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def Same_brand(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('Car', 'Brand_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('Car', 'Brand_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('car1') != context.lookup_data('car2') and context.lookup_data('Brand1') == context.lookup_data('Brand2') and context.lookup_data('Brand1') not in (1,2,3,4,5,6,7,8,9):
              engine.assert_('Car', 'siblings',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),
                              rule.pattern(3).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def Same_Country(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('Car', 'country_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('Car', 'country_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('car1') != context.lookup_data('car2') and context.lookup_data('country') == context.lookup_data('country1') and context.lookup_data('country') not in (1,2,3,4,5,6,7,8,9):
              engine.assert_('Car', 'siblings',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),
                              rule.pattern(3).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def how_related_siblings(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('Car', 'siblings', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('Car', 'how_related',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_example')
  
  fc_rule.fc_rule('Same_category', This_rule_base, Same_category,
    (('Car', 'Category_of',
      (contexts.variable('car1'),
       contexts.variable('Category1'),),
      False),
     ('Car', 'Category_of',
      (contexts.variable('car2'),
       contexts.variable('Category2'),),
      False),),
    (contexts.variable('car1'),
     contexts.variable('car2'),
     pattern.pattern_literal('Same_Category'),
     contexts.variable('Category1'),))
  
  fc_rule.fc_rule('Select_Category', This_rule_base, Select_Category,
    (('Car', 'Category_of',
      (contexts.variable('Category'),
       contexts.variable('car1'),),
      False),),
    (contexts.variable('car1'),
     pattern.pattern_literal('car2'),
     pattern.pattern_literal('Same_Category'),
     contexts.variable('Category'),))
  
  fc_rule.fc_rule('Same_brand', This_rule_base, Same_brand,
    (('Car', 'Brand_of',
      (contexts.variable('car1'),
       contexts.variable('Brand1'),),
      False),
     ('Car', 'Brand_of',
      (contexts.variable('car2'),
       contexts.variable('Brand2'),),
      False),),
    (contexts.variable('car1'),
     contexts.variable('car2'),
     pattern.pattern_literal('Same_brand'),
     contexts.variable('Brand2'),))
  
  fc_rule.fc_rule('Same_Country', This_rule_base, Same_Country,
    (('Car', 'country_of',
      (contexts.variable('car1'),
       contexts.variable('country'),),
      False),
     ('Car', 'country_of',
      (contexts.variable('car2'),
       contexts.variable('country1'),),
      False),),
    (contexts.variable('car1'),
     contexts.variable('car2'),
     pattern.pattern_literal('Same_Country'),
     contexts.variable('country'),))
  
  fc_rule.fc_rule('how_related_siblings', This_rule_base, how_related_siblings,
    (('Car', 'siblings',
      (contexts.variable('person1'),
       contexts.variable('person2'),
       contexts.variable('p2_type'),
       contexts.variable('p1_type'),),
      False),),
    (contexts.variable('person1'),
     contexts.variable('person2'),
     pattern.pattern_tuple((contexts.variable('p1_type'), contexts.variable('p2_type'),), None),))


Krb_filename = '..\\fc_example.krb'
Krb_lineno_map = (
    ((12, 16), (34, 34)),
    ((17, 21), (35, 35)),
    ((22, 22), (36, 36)),
    ((23, 27), (38, 38)),
    ((36, 40), (42, 42)),
    ((41, 45), (45, 45)),
    ((54, 58), (50, 50)),
    ((59, 63), (51, 51)),
    ((64, 64), (52, 52)),
    ((65, 69), (54, 54)),
    ((78, 82), (58, 58)),
    ((83, 87), (59, 59)),
    ((88, 88), (60, 60)),
    ((89, 93), (62, 62)),
    ((102, 106), (72, 72)),
    ((107, 110), (74, 74)),
)
