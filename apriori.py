from efficient_apriori import apriori
transactions = [('onion', 'potato', 'bread','burger'),
                ('onion','potato','burger','coffee'),
                ('onion','potato','coffee')]


itemsets, rules = apriori(transactions ,min_support=0, min_confidence=0)


rules_rhs = filter(lambda rule: len(rule.lhs) == 1 and len(rule.rhs) == 1, rules)
for rule in sorted(rules_rhs, key=lambda itemsets: transactions):
  print(rule)
