# coding=utf-8

from ogb_lite.linkproppred import LinkPropPredDataset

dataset = LinkPropPredDataset(name="ogbl-ppa")

split_edge = dataset.get_edge_split()
train_edge, valid_edge, test_edge = split_edge["train"], split_edge["valid"], split_edge["test"]
graph = dataset[0]  # graph: library-agnostic graph object

print(graph)
print(train_edge, valid_edge, test_edge)