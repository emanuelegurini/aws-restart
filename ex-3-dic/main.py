#!/usr/bin/env python3

#=========================
#=== Esercizio 1
#=========================

server_list: list[str] = ["web01", "db01", "cache01"]

server_list.append("backup01")

server_list.insert(0, "proxy01")

server_list.remove("cache01")

print(server_list)
print(len(server_list))

#=========================
#=== Esercizio 3
#=========================
