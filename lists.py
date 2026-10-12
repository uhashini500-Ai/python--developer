justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

print("1. Original List:")
print(justice_league)

print("\n2. Number of Members:")
print(len(justice_league))

justice_league.extend(["Batgirl", "Nightwing"])

print("\n3. After Adding Batgirl and Nightwing:")
print(justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print("\n4. After Making Wonder Woman the Leader:")
print(justice_league)

hero = "Green Lantern"
justice_league.remove(hero)

position = justice_league.index("Aquaman")
justice_league.insert(position + 1, hero)

print("\n5. After Moving Green Lantern:")
print(justice_league)

justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]

print("\n6. After Replacing the Team:")
print(justice_league)

justice_league.sort()

print("\n7. Alphabetically Sorted Team:")
print(justice_league)

print("\n8. New Leader:")
print(justice_league[0])