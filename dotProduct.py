import numpy as np

input_vector = [1.72, 1.23]
weights_1 = [1.26, 0]
weights_2 = [2.17, 0.32]

# computing the dot product of input_vector and weights_1

first_indexes_mult = input_vector[0] * weights_1[0]
second_indexes_mult = input_vector[1] * weights_2[1]
dot_product_1 = first_indexes_mult + second_indexes_mult

print(f"the manual dot product 1 is: {dot_product_1}")

dot_product_1 = np.dot(input_vector, weights_1)

print(f"the numpy dot product 1 is: {dot_product_1}")

dot_product_2 = np.dot(input_vector, weights_2)

print(f"the dot product 2 is: {dot_product_2}")
