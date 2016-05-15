# nx2d3

Display NetworkX graphs inline in Jupyter notebooks

## Installing

For users:

`$ pip install git+https://github.com/cthoyt/nx2d3.git`

For developers:

`$ git clone https://github.com/cthoyt/nx2d3.git; pip install -e .`

## Sample Code

```python
import networkx as nx
import nx2d3
G = nx.petersen_graph()
nx2d3.embed_networkx(G)
```
