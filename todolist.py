"""
TODO LIST

1  [ ]  Item 1
2  [ ]  Item 2
3  [ ]  Item 3
4  [ ]  Item 4

command >> 
  - add <str>
  - check <int>
  - del <int>
  - exit
"""

List_Item = []


def Add_Item(item_name):
  List_Item.append([item_name, False])


def Display_Item():
  for index, item in enumerate(List_Item):
    status = "[x]" if item[1] else "[ ]"
    print(f"{index+1} {status} {item[0]}")


def Delete_Item(item_index):
  for index, item in enumerate(List_Item):
    if index == item_index:
      List_Item.pop(index)
      return


def Check_Item(item_index):
  for index, item in enumerate(List_Item):
    if index == item_index:
      List_Item[index][1] = not List_Item[index][1]
      return


def main():
  while True:
    print("==================================")
    print("TODO LIST")
    print("")
    Display_Item()
    print("")

    command = input("command >> ").strip().split(" ", maxsplit=1)
    ln_cmd = len(command)

    if ln_cmd == 0:
      continue
    elif ln_cmd == 1:
      action = command[0]

      if action == "exit":
        break
    elif ln_cmd == 2:
      action = command[0]

      if action == "add":
        Add_Item(command[1])
      elif action == "check" and command[1].isdigit():
        Check_Item(int(command[1])-1)
      elif action == "del" and command[1].isdigit():
        Delete_Item(int(command[1])-1)


main()
