tree = [[3, 12, 8],[2,4,6],[14,5,2]]

root = 0
pruned = 0
visited = 0

def children(branch, depth, alpha, beta):
  global tree
  global root
  global pruned
  global visited

  i = 0

  for child in branch:
    if type(child) is list:
      (nalpha, nbeta) = children(child, depth+1, alpha, beta)
      if depth % 2 == 1:
        beta = nalpha if nalpha < beta else beta
        visited += 1
      else:
        alpha = nbeta if nbeta > alpha else alpha
      branch[i] = alpha if depth & 2 == 0 else beta
      visited += 1
    else:
      if depth % 2 == 0 and alpha < child:
        alpha = child
      if depth % 2 == 1 and beta > child:
        beta = child
      if alpha >= beta:
        pruned += 1
        break
  if depth == root:
    tree = alpha if root == 0 else beta
    visited += 1
  return (alpha, beta)

def alphabeta(in_tree = tree, start = root, upper = -15, lower = 15):
  (alpha, beta) = children(tree, start, upper, lower)

  if __name__ == "__main__":
    print("Result: ", tree)
    print("Pruned Nodes: ", pruned)
  return (alpha, beta, tree, pruned)

if __name__ == "__main__":
  alphabeta(None)