def ft_filter(function, inputs) -> list:
    """
    Filter elements of a list using a function.

    Args:
        function: A function that returns a boolean.
        inputs: A list of elements.

    Returns:
        A list of elements that satisfy the condition.
    """
    return [item for item in inputs if function(item)]
