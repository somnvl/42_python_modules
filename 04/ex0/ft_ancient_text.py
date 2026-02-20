#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_ancient_text.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/19 17:23:52 by somenvie            #+#    #+#            #
#   Updated: 2026/02/20 16:56:04 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    try:
        file = "ancient_fragment.txt"
        print(f"Accessing Storage Vault: {file}")
        with open(file) as f:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            data = f.read()
            print(f"{data}")
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("\nERROR: Storage vault not found.")
