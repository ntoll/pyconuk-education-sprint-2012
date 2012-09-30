import sys

row0_cell0 = '-'
row0_cell1 = '-'
row0_cell2 = '-'
row1_cell0 = '-'
row1_cell1 = '-'
row1_cell2 = '-'
row2_cell0 = '-'
row2_cell1 = '-'
row2_cell2 = '-'

def check_winner():

    # Check rows.
    
    if ( row0_cell0 == 'X' and row0_cell1 == 'X' and row0_cell2 == 'X' ):
        print "X Wins!"
        sys.exit()
    if ( row1_cell0 == 'X' and row1_cell1 == 'X' and row1_cell2 == 'X' ):
        print "X Wins!"
        sys.exit()
    if ( row2_cell0 == 'X' and row2_cell1 == 'X' and row2_cell2 == 'X' ):
        print "X Wins!"
        sys.exit()

    # Check Columns
    
    if ( row0_cell0 == 'X' and row1_cell0 == 'X' and row2_cell0 == 'X' ):
        print "X Wins!"
        sys.exit()
    if ( row0_cell1 == 'X' and row1_cell1 == 'X' and row2_cell1 == 'X' ):
        print "X Wins!"
        sys.exit()
    if ( row0_cell2 == 'X' and row1_cell2 == 'X' and row2_cell2 == 'X' ):
        print "X Wins!"
        sys.exit()

    # Check diagonals
    
    if ( row0_cell0 == 'X' and row1_cell1 == 'X' and row2_cell2 == 'X' ):
        print "X Wins!"
        sys.exit()
    if ( row0_cell2 == 'X' and row1_cell1 == 'X' and row2_cell0 == 'X' ):
        print "X Wins!"
        sys.exit()

    
    # Check rows.
    
    if ( row0_cell0 == '0' and row0_cell1 == '0' and row0_cell2 == '0' ):
        print "0 Wins!"
        sys.exit()
    if ( row1_cell0 == '0' and row1_cell1 == '0' and row1_cell2 == '0' ):
        print "0 Wins!"
        sys.exit()
    if ( row2_cell0 == '0' and row2_cell1 == '0' and row2_cell2 == '0' ):
        print "0 Wins!"
        sys.exit()

    # Check Columns
    
    if ( row0_cell0 == '0' and row1_cell0 == '0' and row2_cell0 == '0' ):
        print "0 Wins!"
        sys.exit()
    if ( row0_cell1 == '0' and row1_cell1 == '0' and row2_cell1 == '0' ):
        print "0 Wins!"
        sys.exit()
    if ( row0_cell2 == '0' and row1_cell2 == '0' and row2_cell2 == '0' ):
        print "0 Wins!"
        sys.exit()

    # Check diagonals
    
    if ( row0_cell0 == '0' and row1_cell1 == '0' and row2_cell2 == '0' ):
        print "0 Wins!"
        sys.exit()
    if ( row0_cell2 == '0' and row1_cell1 == '0' and row2_cell0 == '0' ):
        print "0 Wins!"
        sys.exit()


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

    check_winner()
    
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

    check_winner()



