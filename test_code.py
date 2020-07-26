from .problem3 import (
    find_lca, 
    Node, 
    node2,
    node3, 
    node4,
    node5, 
    node6, 
    node7,
    node8,
    node9,
    root
)

def test_anchestor():
    anchestor = find_lca(node2, node3)
    assert anchestor == root.value

    anchestor = find_lca(node7, node3)
    assert anchestor == node3.value
    assert anchestor != node7.value

    anchestor = find_lca(node8, node5)
    assert anchestor == node2.value