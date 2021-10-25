// Note: does not compile! assumes negative numbers are after positive numbers in list
Node removeCancellableNodes(Node listHead)
{
	if (listHead == null) return null; // or listHead
	Stack<Node> stack = new Stack<Node>();
	Node node = listHead;  	
	while(node != null)
	{
		if (node.value < 0)
		{
			int sum = node.value;
                        while (!stack.isEmpty())
			{
				Node temp = stack.pop();
				sum -= temp.value;
				temp = null;
				if (sum == 0)
				{
					node = stack.peek();
					break;
				}
			}
		}
		else
		{
			stack.push(node);
		}
		node = node.next;
	}
	
	return listHead;
}
