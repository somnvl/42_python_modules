#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_vault_security.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/20 17:23:43 by somenvie            #+#    #+#            #
#   Updated: 2026/02/20 17:48:42 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    try:
        print("Initiating secure vault access...")
        file = "classified_data.txt"
        with open(file, "r") as f:
            print("Vault connection established with failsafe protocols\n")

            print("SECURE EXTRACTION:")
            data = f.read()
            print(data)

        with open("security_protocols.txt", "w") as f:
            print("\nSECURE PRESERVATION:")
            data = "[CLASSIFIED] New security protocols archived"
            f.write(data)
            print(data)

        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")

    except FileNotFoundError:
        print("\nERROR: Storage vault not found.")
