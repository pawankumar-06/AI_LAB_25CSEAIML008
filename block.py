from collections import deque

#function to check whether a block is clear 
def is_clear (state,block):
    for b, position in state:
        if position == block:
            return False
    return True

#generate possible moves
def generate_moves(state,blocks):
    moves = []
    for block in blocks:
        #block must be clear
        if not is_clear(state,block):
            continue
        #find current position
        current_position =None
        for b, position in state:
            if b== block:
                current_position=position
                break
        #move block to table
        if current_position!= "Table":
            new_state = set(state)
            new_state.remove((block,current_position))
            new_state.add((block,"Table"))

            moves.append(
                (frozenset(new_state),f"Move {block} from {current_position} to Table")
            )
            #move block onto another block
            for destination in blocks:
                if block= destination:
                    continue
                #destination must be clear
                if not is_clear(state,destination):
                    continue
                #don't move to the same position
                if current_position == destination:
                    continue
                new_state=set(state)

                new_state.remove((block,current_position))
                new_state.add((block,destination))