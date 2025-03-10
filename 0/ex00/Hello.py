# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oabdelka <oabdelka@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 01:11:43 by oabdelka          #+#    #+#              #
#    Updated: 2025/03/10 20:24:02 by oabdelka         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "world!"
ft_tuple = {"Hello", "Lebanon"}
ft_set.remove("tutu!")
ft_set.add("Beirut!")
ft_dict["Hello"] = "42Beirut!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
