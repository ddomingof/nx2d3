# nx2d3

Display NetworkX graphs inline in Jupyter notebooks

## Installing

For users:

`$ pip install git+https://github.com/cthoyt/nx2d3.git`

For developers:

`$ git clone https://github.com/cthoyt/nx2d3.git; pip install -e .`

## Example

```python
import networkx as nx
import nx2d3
G = nx.petersen_graph()
nx2d3.embed_networkx(G)
```

**Note:** GitHub will not render custom javascript on https://github.com/cthoyt/nx2d3/blob/master/example.ipynb. 
Instead, try nbviewer http://nbviewer.jupyter.org/github/cthoyt/nx2d3/blob/master/example.ipynb or viewing the
notebooks in jupyter notebook locally.
