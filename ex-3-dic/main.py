#!/usr/bin/env python3

#=========================
#=== Esercizio 1
#=========================

server_list: list[str] = ["web01", "db01", "cache01"]

server_list.append("backup01")

server_list.insert(0, "proxy01")

server_list.remove("cache01")

## print(server_list)
## print(len(server_list))

#=========================
#=== Esercizio 3
#=========================

price_list_u: list[float] = [45.5, 12.0, 78.3, 23.1, 56.7]

price_list_o: list[float] = sorted(price_list_u)

# print(price_list_o)

# print(min(price_list_o))
# print(max(price_list_o))

# print( 23.1 in price_list_o)

counter = 0

# print(sum(1 for p in price_list_o if p > 50))


#=========================
#=== Esercizio 7
#=========================


