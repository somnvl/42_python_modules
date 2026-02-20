#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_crisis_response.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/20 17:49:48 by somenvie            #+#    #+#            #
#   Updated: 2026/02/20 18:09:26 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def crisis_handler(file: str, crisis: bool) -> str | None:
    if crisis:
        print(f"CRISIS ALERT: Attempting access to '{file}'...")
    else:
        print(f"ROUTINE ACCESS: Attempting access to '{file}'...")
    try:
        with open(file) as f:
            data = f.read()
            return data
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM  ===\n")

    crisis_handler("lost_archive.txt", True)
    print("STATUS: Crisis handled, system stable\n")
    crisis_handler("classified_vault.txt", True)
    print("STATUS: Crisis handled, security maintained\n")
    data = crisis_handler("standard_archive.txt", False)
    if data:
        print(f"SUCCESS: Archive recovered - ``{data}''")
        print("STATUS: Normal operations resumed\n")

    print("All crisis scenarios handled successfully. Archives secure.")
