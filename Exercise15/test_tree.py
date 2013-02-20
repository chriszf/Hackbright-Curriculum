import exercise11 as ex11

def test_basic_tree():
    root = ex11.BinaryTreeNode(5)
    assert root.get_value() == 5
    assert root.get_left() == None
    assert root.get_right() == None

def test_simple_tree():
    root = ex11.BinaryTreeNode(0)
    left = ex11.BinaryTreeNode(1)
    right = ex11.BinaryTreeNode(2)

    root.set_left(left)
    root.set_right(right)
   
    assert root.get_left() == left
    assert root.get_right() == right
    assert left.get_left() == None
    assert right.get_right() == None
    assert root.get_left().get_value() == 1
    assert root.get_right().get_value() == 2
    assert root.get_value() == 0

def test_depth_first(capsys):
    root = ex11.BinaryTreeNode(0)
    left = ex11.BinaryTreeNode(1)
    right = ex11.BinaryTreeNode(4)
    l_left = ex11.BinaryTreeNode(2)
    l_right = ex11.BinaryTreeNode(3)
    r_left = ex11.BinaryTreeNode(5)
    r_right = ex11.BinaryTreeNode(6)
    
    ex11.depth_first_traversal(root)
    out, err = capsys.readouterr()
    expected = "1 2 3 4 5 6"
    print "Your output", out
    print "Expected output", expected

    assert out == "1 2 3 4 5 6"
