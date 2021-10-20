# alpha/maximizer goes to left side
# beta/minimizer goes to right side
# working of the alpha-beta pruning

# initial values of aplha & beta
tree = [[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]
root = 0
pruned = 0

# return optimal value for current player
# (Initially called for the root and maximizer)

def children(branch, depth, alpha, beta):
	global tree
	global root
	global pruned
	i = 0
	for child in branch:
		if type(child) is list:
			(nalpha, nbeta) = children(child, depth + 1, alpha, beta)
			if depth % 2 == 1:
				beta = nalpha if nalpha < beta else beta
			else:
				alpha = nbeta if nbeta > alpha else alpha
				branch[i] = alpha if depth % 2 == 0 else beta
				i += 1
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
	return (alpha, beta)

def alphabeta(in_tree=tree, start=root, upper=-15, lower=15):
	global tree
	global pruned
	global root
	(alpha, beta) = children(tree, start, upper, lower)

	if __name__ == "__main__":
		print ("(alpha, beta): ", alpha, beta)
		print ("Result: ", tree)
		print ("Times pruned: ", pruned)
	return (alpha, beta, tree, pruned)
if __name__ == "__main__":
	alphabeta(None)
  
  
#   output of this file 
# (alpha, beta):  5 15
# Result:  5
# Times pruned:  1

