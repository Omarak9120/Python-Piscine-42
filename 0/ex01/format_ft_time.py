# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oabdelka <oabdelka@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 01:11:35 by oabdelka          #+#    #+#              #
#    Updated: 2025/03/10 01:39:35 by oabdelka         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import datetime

current_time = time.time()
current_date = datetime.datetime.now()
print(f"Seconds since January 1, 1970: {current_time:,.4f} or {current_time:.2e} in scientific notation")
print(current_date.strftime("%b %d %Y"))

