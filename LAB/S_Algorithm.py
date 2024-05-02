def find_s_algorithm(examples):
    num_attributes = len(examples[0]) - 1
    hypothesis = ['0'] * num_attributes

    for example in examples:
        if example[-1] == '1':
            for i in range(num_attributes):
                if hypothesis[i] == '0':
                    hypothesis[i] = example[i]
                elif hypothesis[i] != example[i]:
                    hypothesis[i] = '?'

    return hypothesis


training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', '0'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', '1'],
    ['Rainy', 'Cold', 'High', 'Weak', 'Warm', 'Change', '0'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', '1']
]

hypothesis_result = find_s_algorithm(training_data)
print('Hypothesis', hypothesis_result)
