# Create empty list 
shopping_list = []


# create a function to show help text
def show_help():
  print("What should we pick up at the store?")
  print("""
  Enter 'DONE' to stop adding items.
  Enter 'HELP' for this help.
  Enter 'SHOW' to show your current list.
  """)


# create a function to add item to list
def add_to_list(item):
  shopping_list.append(item)
  # notify user that item was added, and number of items in list
  print("Added! List has {} items.".format(len(shopping_list)))


# create a function to show the list
def show_list():
  print("Here's your list:")
  for item in shopping_list:
    print(item)

# run it all with conditions
show_help()
# this will always happen so we have to use control flow (break, continue)
# another way to do this is to use an else but I didn't so I could use break and continue
while True:
  new_item = input("> ")
  if new_item == 'DONE':
    break
  elif new_item == 'HELP':
    show_help()
    continue
  # enable show function
  elif new_item == 'SHOW':
    show_list()
    continue

  # call add list function
  add_to_list(new_item)

# show your list when DONE
show_list()