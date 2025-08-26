print("Tower of Honoi !!")

n_disk = 3
main_tower = "A"
temp_tower = "B"
target_tower = "C"
def tower_of_honoi(n,main,temp,target):
    if n == 1:
        print(f"Disk No. 1 Move from {main} -> {target}")
        return

    tower_of_honoi(n-1,main,target,temp)
    print(f"Disk No. {n} Move from {main} -> {target}")
    tower_of_honoi(n-1,temp,main,target)


tower_of_honoi(n_disk,main_tower,temp_tower,target_tower)