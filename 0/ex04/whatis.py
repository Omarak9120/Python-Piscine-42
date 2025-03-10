# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oabdelka <oabdelka@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 15:23:23 by oabdelka          #+#    #+#              #
#    Updated: 2025/03/10 15:40:03 by oabdelka         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def odd_even(number):
	if number % 2 == 0:
		return "I'm Even."
	else:
		return "I'm Odd."

try:
    if len(sys.argv) != 2:
        raise AssertionError("Incorrect number of arguments" if len(sys.argv) > 2 else "")

    number = int(sys.argv[1])

    print(odd_even(number))

except ValueError:
    print("AssertionError: Argument is not an integer")

except AssertionError as error:
    if str(error):
        print(f"AssertionError: {error}")