- We can break the problem down into two arrays
    - We construct two arrays, each representing the potential fall of the direction (right/left)
        - Algorithm:
            ```
                if dominoes[i] == 'L/R':
                    dist = 1
                    prev = 'L/R'
                elif dominoes[i] != '.':
                    prev = dominoes[i]
                elif dominoes[i] == '.' and prev == 'L/R'
                    right/left[i] = dist
                    dist += 1
            ```
    - Then it's trivial to figure out the conditions
        - Note: comparing `right[i]` against `left[i]` the "smallest" wins, as it's the closest to a falling dominoe
- Can we break the problem down to using two pointers?