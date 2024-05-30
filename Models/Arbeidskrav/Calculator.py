#oppgavesett 3 oppgave 1

class Calculator:

  def add(self, a, b, c=None):
    if c is not None:
      return a + b + c
    else:
      return a + b


calculator = Calculator()

sum_to_tall = calculator.add(5, 3)
print(f"Summen av tallene er: {sum_to_tall}")

sum_tre_tall = calculator.add(10, 20, 30)
print(f"Summen av tallene er: {sum_tre_tall}")
