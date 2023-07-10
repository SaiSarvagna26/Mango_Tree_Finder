rows=int(input())
columns=int(input())
tree_no=int(input())
total=rows*columns
if tree_no<1 or tree_no>total:
    print("Invalid")
else:
    if tree_no<=columns or(tree_no-1)%columns==0:
        print("true")
    else:
        print("false")