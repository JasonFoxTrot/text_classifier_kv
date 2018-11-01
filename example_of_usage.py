import text_classifier_kv as docclass


def sampletrain(cl: docclass.classifier) -> None:
    cl.train('Nobody owns the water.', 'good')
    cl.train('the quick rabbit jumps fences', 'good')
    cl.train('buy pharmaceuticals now', 'bad')
    cl.train('make quick money at the online casino', 'bad')
    cl.train('the quick brown fox jumps', 'good')
    cl.train('python is programming language', 'good')
    return None


cl: docclass.classifier = docclass.classifier()
sampletrain(cl)

print('1 ...')
# тест обучения
r = cl.fprob('money', 'good')
print('is money good: ' + str(r))
r = cl.fprob('money', 'bad')
print('is money bad: ' + str(r))

print('2 ...')
# тест обучения с использование взвещенной вероятностью
r = cl.weightedprob('money', 'good', cl.fprob)
print('is money good: ' + str(r))
r = cl.weightedprob('money', 'bad', cl.fprob)
print('is money bad: ' + str(r))

cl = docclass.naivebayes()
sampletrain(cl)

print('3 ...')
# вероятность попадания в категорию в Байерсу
r = cl.prob('python money', 'good')
print('is money good: ' + str(r))
r = cl.prob('python money', 'bad')
print('is money bad: ' + str(r))


print('4 ...')
cl = docclass.naivebayes()
sampletrain(cl)
# автоматическая классификация
cat: str = cl.classify('quick rabbit')
print('cat for quick rabbit: ' + cat)
cat = cl.classify('quick money')
print('cat for quick money: ' + cat)
# плюс порог
cl.setthreshold('bad', 3.0)
cat = cl.classify('quick money')
print('cat for quick money: ' + cat)
for i in range(10):
    sampletrain(cl)
cat = cl.classify('quick money')
print('cat for quick money: ' + cat)

print('5 ...')
cl = docclass.fisherclassifier()
sampletrain(cl)
r = cl.cprob('quick', 'good')
print('is quick good: ' + str(r))
r = cl.cprob('money', 'bad')
print('is money bad: ' + str(r))

print('6 ...')
r = cl.fisherprob('quick rabbit', 'good')
print('is quick rabbit good: ' + str(r))
r = cl.fisherprob('quick rabbit', 'bad')
print('is quick rabbit bad: ' + str(r))

print('7 ...')
cat = cl.classify('quick rabbit')
print('cat for quick rabbit: ' + cat)
cat = cl.classify('quick money')
print('cat for quick money: ' + cat)
