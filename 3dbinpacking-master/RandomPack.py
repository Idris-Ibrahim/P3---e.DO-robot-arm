import random 

# Define a list of packages
packages = [100, 70, 120, 40, 80, 90]

# Define the volume of the shipping box
box_volume = 200

def packing_algorithm(packages, box_volume):
    # Set the list of available packages to the list of packages provided
    available_packages = packages

    while len(available_packages) > 0:
        # Randomly select a package from the list of available packages
        package = random.choice(available_packages)

        # If the selected package fits into the shipping box:
        if package <= box_volume:
            # Randomly place the package in the shipping box
            x, y, z = random.randint(0, box_volume - package[0]), random.randint(0, box_volume - package[1]), random.randint(0, box_volume - package[2])
            box_volume[x:x + package[0], y:y + package[1], z:z + package[2]] = package
            available_packages.remove(package)

    # Calculate and print the remaining volume in the box
    remaining_volume = box_volume.count(0)
    print("Remaining volume: ", remaining_volume)

    # Print the configuration of packages in the box
    print(available_packages)

    # Return the configuration of packages in the box as the output
    return available_packages