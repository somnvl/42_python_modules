#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_archive_creation.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: somenvie <somenvie@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/20 16:43:51 by somenvie            #+#    #+#            #
#   Updated: 2026/02/20 17:14:23 by somenvie           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    try:
        file = "new_discovery.txt"
        print(f"Initializing new storage unit: {file}")
        with open(file, "x") as f:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            data = (
                "[ENTRY 001] New quantum algorithm discovered\n"
                "[ENTRY 002] Efficiency increased by 347%\n"
                "[ENTRY 003] Archived by Data Archivist trainee\n"
            )
            f.write(data)
            print(data)
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{file}' ready for long-term preservation.")
    except FileExistsError:
        print("\nERROR: Archive already exists")
