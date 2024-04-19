numbers=[[1,2,3],[4,5,6],[7,8,9]]
results=[ ]
for k in numbers:
    for result in k:
        if int(result) %2 == 0:
            results.append(result)
print(results)
