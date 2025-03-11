from give_bmi import give_bmi, apply_limit
height = [1.8, 1.8]
weight = [72, 72]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
