def NULL_not_found(object: any) -> int:
	if object is None:
		print("Nothing:", object, type(object))
	elif isinstance(object, float) and object != object:  # Check for NaN
		print("Cheese:", object, type(object))
	elif isinstance(object, bool):
		print("Fake:", object, type(object))
	elif object == 0:
		print("Zero:", object, type(object))
	elif isinstance(object, str) and len(object) == 0:
		print("Empty:", type(object))
	else:
		print("Type not Found")
		return 1
	return 0
