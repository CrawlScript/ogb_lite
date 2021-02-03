# coding=utf-8
from ogb_lite.nodeproppred import NodePropPredDataset

dataset = NodePropPredDataset(name="ogbn-proteins")

split_idx = dataset.get_idx_split()
train_idx, valid_idx, test_idx = split_idx["train"], split_idx["valid"], split_idx["test"]
graph, label = dataset[0] # graph: library-agnostic graph object

print(graph, label)
print(train_idx, valid_idx, test_idx)