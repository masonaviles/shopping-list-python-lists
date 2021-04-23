musical_groups = [
    ["Ad Rock", "MCA", "Mike D."],
    ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
    ["Salt", "Peppa", "Spinderella"],
    ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
    ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
    ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
    ["Run", "DMC", "Jam Master Jay"],
]
# Here is a multi-dimensional list of musical groups. The first dimension is group, the second is group members.
# Can you loop through each group and output the members joined together with a ", " comma space as a separator, please?

for group in musical_groups:
    print(", ".join(group))

# Awesome! Now I'd like to see only groups that are trios, you know 3 members.
# So can you please only print out the trios? It should still use the joined string format from task 1.

for group in musical_groups:
    if len(group) == 3:
      print(", ".join(group))