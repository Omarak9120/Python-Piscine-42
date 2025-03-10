# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#     tester.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oabdelka <oabdelka@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 02:19:56 by oabdelka          #+#    #+#              #
#    Updated: 2025/03/10 02:19:57 by oabdelka         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from find_ft_type import all_thing_is_obj
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
# print()
print(all_thing_is_obj(10))