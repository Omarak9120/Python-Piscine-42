# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oabdelka <oabdelka@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 15:23:28 by oabdelka          #+#    #+#              #
#    Updated: 2025/03/10 15:23:29 by oabdelka         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math

def NULL_not_found(object: any) -> int:
    type_names = {
        None: "Nothing",
        0: "Zero",
        "": "Empty",
        False: "Fake"
    }

    if isinstance(object, float) and math.isnan(object):
        print(f"Cheese: nan <class 'float'>$")
        return 0

    if object in type_names:
        print(f"{type_names[object]}: {object} <class '{type(object).__name__}'>")
        return 0

    print("Type not Found")
    return 1
