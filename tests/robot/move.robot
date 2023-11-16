*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position. \n\n https://raw.githubusercontent.com/level-up-program/team-12-arch-city-pythons-e904776a/main/tests/robot/images/Move%20spec%20by%20example%201.jpeg \n\n https://raw.githubusercontent.com/level-up-program/team-12-arch-city-pythons-e904776a/main/tests/robot/images/Move%20spec%20by%20example%202.jpeg
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
BottomLeftCornerMoveNorth   	0	0	3	North	0	1	4
BottomLeftCornerMoveEast	    0	0	4	East	1	0	5
BottomLeftCornerMoveSouth	    0	0	7	South	0	0	8
BottomLeftCornerMoveWest    	0	0	12	West	0	0	13
LeftWallMoveNorth   	0	4	32	North	0	5	33
LeftWallMoveEast    	0	4	46	East	1	4	47
LeftWallMoveSouth   	0	4	89	South	0	3	90
LeftWallMoveWest    	0	4	76	West	0	4	77
TopLeftCornerMoveNorth  	0	9	43	North	0	9	44
TopLeftCornerMoveEast	    0	9	22	East	1	9	23
TopLeftCornerMoveSouth	    0	9	34	South	0	8	35
TopLeftCornerMoveWest	    0	9	5	West	0	9	6
BottomWallMoveNorth	    4	0	67	North	4	1	68
BottomWallMoveEast	    4	0	89	East	5	0	90
BottomWallMoveSouth	    4	0	42	South	4	0	43
BottomWallMoveWest	    4	0	2	West	3	0	3
MiddleOfMapMoveNorth	    4	4	23	North	4	5	24
MiddleOfMapMoveEast	    4	4	13	East	5	4	14
MiddleOfMapMoveSouth    	4	4	1	South	4	3	2
MiddleOfMapMoveWest 	4	4	7	West	3	4	8
TopWallMoveNorth    	4	9	8	North	4	9	9
TopWallMoveEast 	4	9	36	East	5	9	37
TopWallMoveSouth    	4	9	789	South	4	8	790
TopWallMoveWest 	4	9	12	West	3	9	13
BottomRightCornerMoveNorth  	9	0	3	North	9	1	4
BottomRightCornerMoveEast   	9	0	48	East	9	0	49
BottomRightCornerMoveSouth  	9	0	65	South	9	0	66
BottomRightCornerMoveWest   	9	0	56	West	8	0	57
RightWallMoveNorth  	9	4	39	North	9	5	40
RightWallMoveEast   	9	4	89	East	9	4	90
RightWallMoveSouth  	9	4	60	South	9	3	61
RightWallMoveWest   	9	4	25	West	8	4	26
TopRightCornerMoveNorth     9	9	73	North	9	9	74
TopRightCornerMoveEast  	9	9	59	East	9	9	60
TopRightCornerMoveSouth 	9	9	99	South	9	8	100
TopRightCornerMoveWest  	9	9	100	West	8	9	101

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}