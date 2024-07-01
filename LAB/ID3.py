import pandas as pd
import math

class Node:
    def __init__(self, attribute=None, result=None):
        self.attribute = attribute
        self.result = result
        self.children = {}


def ID3(examples, attributes, target):
    if len(examples[target].unique()) == 1:
        return Node(result=examples[target].iloc[0])
    if not attributes:
        return Node(result=examples[target].mode()[0])

    best_attr = max(attributes, key=lambda attr: information_gain(examples, attr, target))
    tree = Node(attribute=best_attr)

    for value, subset in examples.groupby(best_attr):
        tree.children[value] = ID3(subset.drop(columns=[best_attr]), attributes - {best_attr}, target)

    return tree


def information_gain(examples, attribute, target_attribute):
    entropy_S = entropy(examples[target_attribute])
    subset_entropy = sum((len(subset) / len(examples)) * entropy(subset[target_attribute])
                         for _, subset in examples.groupby(attribute))
    return entropy_S - subset_entropy


def entropy(attribute_values):
    value_counts = attribute_values.value_counts(normalize=True)
    return -sum(p * math.log2(p) for p in value_counts)


data = {
    'Outlook': ['Sunny', 'Overcast'],
    'Temperature': ['Hot', 'Mild'],
    'PlayTennis': ['No', 'Yes']
}

df = pd.DataFrame(data)
attributes = set(df.columns) - {'PlayTennis'}
tree = ID3(df, attributes, 'PlayTennis')

print("Decision Tree:")
print(tree)

new_sample = {'Outlook': 'Overcast', 'Temperature': 'Mild'}
current_node = tree

while current_node.children:
    attribute_value = new_sample.get(current_node.attribute)
    if attribute_value in current_node.children:
        current_node = current_node.children[attribute_value]
    else:
        break

classification = current_node.result

print("Classification for the new sample:", classification)
