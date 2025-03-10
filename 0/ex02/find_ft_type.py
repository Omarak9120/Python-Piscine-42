# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oabdelka <oabdelka@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 02:19:49 by oabdelka          #+#    #+#              #
#    Updated: 2025/03/10 02:19:50 by oabdelka         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# def all_thing_is_obj(object: any) -> int:
# 	print(f"{type(object).__name__.capitalize()} : {type(object)}")
# 	object_type = type(object)

# 	if object_type == str:
# 		print(f"{object} is in the kitchen : {object_type}")
# 	return(42)

def all_thing_is_obj(object: any) -> int:
	type_names = {
		list: "List",
		tuple: "Tuple",
		set: "Set",
		dict: "Dict",
		str: "String"
	}

	object_type = type(object)
	type_name = type_names.get(object_type, "Type not found")

	if object_type == str:
		print(f"{object} is in the kitchen : {object_type}")
	elif type_name != "Type not found":
		print(f"{type_name} : {object_type}")
	else:
		print(f"{type_name}")

	return 42