
Open Graph Benchmark Lite (ogb_lite)
====================================

Open Graph Benchmark Lite (ogb_lite) is a subset of the ogb project. It supports library-agnostic loaders and it does not require torch. 

99.99% of the code is copied from the OGB project: 


* `https://github.com/snap-stanford/ogb <https://github.com/snap-stanford/ogb>`_

We only make some small changes such that you can use ogb_lite without installing torch.

Installation
------------

.. code-block:: bash

   pip install ogb_lite

Tutorial
--------

ogb_lite only contains three library-agnostic loaders: ``NodePropPredDataset``\ , ``LinkPropPredDataset``\ , and ``GraphPropPredDataset``.

**NodePropPredDataset:**

.. code-block:: python

   # coding=utf-8
   from ogb_lite.nodeproppred import NodePropPredDataset

   dataset = NodePropPredDataset(name="ogbn-proteins")

   split_idx = dataset.get_idx_split()
   train_idx, valid_idx, test_idx = split_idx["train"], split_idx["valid"], split_idx["test"]
   graph, label = dataset[0] # graph: library-agnostic graph object

   print(graph, label)
   print(train_idx, valid_idx, test_idx)

**LinkPropPredDataset:**

.. code-block:: python

   # coding=utf-8

   from ogb_lite.linkproppred import LinkPropPredDataset

   dataset = LinkPropPredDataset(name="ogbl-ppa")

   split_edge = dataset.get_edge_split()
   train_edge, valid_edge, test_edge = split_edge["train"], split_edge["valid"], split_edge["test"]
   graph = dataset[0]  # graph: library-agnostic graph object

   print(graph)
   print(train_edge, valid_edge, test_edge)

**GraphPropPredDataset:**

.. code-block:: python

   # coding=utf-8

   from ogb_lite.graphproppred import GraphPropPredDataset

   dataset = GraphPropPredDataset(name="ogbg-molhiv")

   split_idx = dataset.get_idx_split()
   train_idx, valid_idx, test_idx = split_idx["train"], split_idx["valid"], split_idx["test"]

   graph, label = dataset[0]  # graph: library-agnostic graph object
   print(graph, label)
   print(train_idx, valid_idx, test_idx)

Citing OGB
----------

If you use OGB datasets in your work, please cite the OGB paper (Bibtex below).

.. code-block:: HTML

   @article{hu2020ogb,
     title={Open Graph Benchmark: Datasets for Machine Learning on Graphs},
     author={Weihua Hu, Matthias Fey, Marinka Zitnik, Yuxiao Dong, Hongyu Ren, Bowen Liu, Michele Catasta, Jure Leskovec},
     journal={arXiv preprint arXiv:2005.00687},
     year={2020}
   }
