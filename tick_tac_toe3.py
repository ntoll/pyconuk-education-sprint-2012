row0_cell0 = '-'
row0_cell1 = '-'
row0_cell2 = '-'
row1_cell0 = '-'
row1_cell1 = '-'
row1_cell2 = '-'
row2_cell0 = '-'
row2_cell1 = '-'
row2_cell2 = '-'


while True:
    print row0_cell0, row0_cell1, row0_cell2 
    print row1_cell0, row1_cell1, row1_cell2 
    print row2_cell0, row2_cell1, row2_cell2 
                        
    move=raw_input('Player 1:')

    if move=="0,0":
        row0_cell0 = 'X'
    if move=="0,1":
        row0_cell1 = 'X'
    if move=="0,2":
        row0_cell2 = 'X'
    if move=="1,0":
        row1_cell0 = 'X'
    if move=="1,1":
        row1_cell1 = 'X'
    if move=="1,2":
        row1_cell2 = 'X'
    if move=="2,0":
        row2_cell0 = 'X'
    if move=="2,1":
        row2_cell1 = 'X'
    if move=="2,2":
        row2_cell2 = 'X'

    print row0_cell0, row0_cell1, row0_cell2 
    print row1_cell0, row1_cell1, row1_cell2 
    print row2_cell0, row2_cell1, row2_cell2 

    move=raw_input('Player 2:')

    if move=="0,0":
        row0_cell0 = '0'
    if move=="0,1":
        row0_cell1 = '0'
    if move=="0,2":
        row0_cell2 = '0'
    if move=="1,0":
        row1_cell0 = '0'
    if move=="1,1":
        row1_cell1 = '0'
    if move=="1,2":
        row1_cell2 = '0'
    if move=="2,0":
        row2_cell0 = '0'
    if move=="2,1":
        row2_cell1 = '0'
    if move=="2,2":
        row2_cell2 = '0'



