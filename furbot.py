import random #line:1
import numpy as np #line:2
from ..bot_control import Move #line:3
from copy import copy #line:4
import random #line:5
class FurryBot :#line:8
    def __init__ (O0O00O0OOO00O0OOO ):#line:10
        O0O00O0OOO00O0OOO .target =None #line:11
        O0O00O0OOO00O0OOO .grid_size =None #line:12
        O0O00O0OOO00O0OOO .cross =[[0 ,1 ],[-1 ,0 ],[0 ,-1 ],[1 ,0 ]]#line:13
        O0O00O0OOO00O0OOO .cross +=[[0 ,2 ],[1 ,1 ],[2 ,0 ],[1 ,-1 ],[0 ,-2 ],[-1 ,-1 ],[-2 ,0 ],[-1 ,1 ]]#line:14
        O0O00O0OOO00O0OOO .cross +=[[0 ,3 ],[1 ,2 ],[-2 ,1 ],[-3 ,0 ],[-2 ,-1 ],[-1 ,-2 ],[0 ,-3 ],[1 ,-2 ],[2 ,-1 ],[3 ,0 ],[2 ,1 ],[1 ,2 ]]#line:15
    def get_name (OO0OO00O0O0OOO0O0 ):#line:17
        return "FurryBot"#line:18
    def get_contributor (OO00000O00OO00O0O ):#line:20
        return "Ferdinand Schumacher"#line:21
    def clamp (O00O00OO0O00OOO0O ,OO0OO00OOOOOOO0OO ,O0000000O0O0O0OO0 ,O0OO0OO00O0OOO000 ):#line:23
        return max (O0000000O0O0O0OO0 ,min (OO0OO00OOOOOOO0OO ,O0OO0OO00O0OOO000 ))#line:24
    def get_cell (O00OO0OOO00O00OO0 ,O00OOO000OO0O00O0 ,OOOO0000OOOOOO0O0 ):#line:26
        return O00OOO000OO0O00O0 +OOOO0000OOOOOO0O0 #line:27
    def get_cell_cost (O0OOOOO00OOOO0O0O ,O0OOOO000O000OO0O ,O0O0000O00O00OOO0 ):#line:29
        if O0O0000O00O00OOO0 [0 ]<0 or O0O0000O00O00OOO0 [0 ]>O0OOOOO00OOOO0O0O .grid_size -1 or O0O0000O00O00OOO0 [1 ]<0 or O0O0000O00O00OOO0 [1 ]>O0OOOOO00OOOO0O0O .grid_size -1 :#line:31
            return 1e9 #line:32
        else :#line:33
            O0OO0O0O0O00OOO0O =O0OOOO000O000OO0O [O0O0000O00O00OOO0 [1 ],O0O0000O00O00OOO0 [0 ]]#line:34
            if O0OO0O0O0O00OOO0O ==0 :#line:35
                return 0 #line:36
            else :#line:37
                return [100 ,10 ,0 ][(O0OOOOO00OOOO0O0O .id -O0OO0O0O0O00OOO0O )%3 ]#line:39
    def get_new_target (OOO00000O0O0OO0O0 ,O0OOOOO0O000O0OO0 ):#line:41
        O0OOO00OOOO0OO0O0 =1e9 #line:42
        random .shuffle (OOO00000O0O0OO0O0 .cross )#line:44
        for O0OOO0000OOO00000 in OOO00000O0O0OO0O0 .cross :#line:45
            OOOO0OO0OOO0O00O0 =OOO00000O0O0OO0O0 .get_cell (OOO00000O0O0OO0O0 .position ,O0OOO0000OOO00000 )#line:47
            O0O0O000OO0OO0O0O =OOO00000O0O0OO0O0 .get_cell_cost (O0OOOOO0O000O0OO0 ,OOOO0OO0OOO0O00O0 )#line:49
            if O0O0O000OO0OO0O0O <O0OOO00OOOO0OO0O0 :#line:50
                O0OOO00OOOO0OO0O0 =O0O0O000OO0OO0O0O #line:51
                OOO00000O0O0OO0O0 .target =OOOO0OO0OOO0O00O0 #line:52
        if O0OOO00OOOO0OO0O0 >0 :#line:54
            OOO00000O0O0OO0O0 .target [0 ]=random .randint (0 ,O0OOOOO0O000O0OO0 .shape [0 ]-1 )#line:55
            OOO00000O0O0OO0O0 .target [1 ]=random .randint (0 ,O0OOOOO0O000O0OO0 .shape [1 ]-1 )#line:56
    def determine_next_move (O0OOO00O00O0O0000 ,O000OO0OO00O00O0O ,O0000O00O0OO0OO0O ,OO00O0OOOO00OOO00 ):#line:58
        if O0OOO00O00O0O0000 .grid_size ==None :#line:60
            O0OOO00O00O0O0000 .grid_size =OO00O0OOOO00OOO00 .grid_size #line:61
        if O0OOO00O00O0O0000 .target is None :#line:64
            O0OOO00O00O0O0000 .target =copy (O0OOO00O00O0O0000 .position )#line:65
        if np .array_equal (O0OOO00O00O0O0000 .position ,O0OOO00O00O0O0000 .target ):#line:68
            O0OOO00O00O0O0000 .get_new_target (O000OO0OO00O00O0O )#line:69
        if O0OOO00O00O0O0000 .target [0 ]>O0OOO00O00O0O0000 .position [0 ]:#line:72
            return Move .RIGHT #line:73
        elif O0OOO00O00O0O0000 .target [0 ]<O0OOO00O00O0O0000 .position [0 ]:#line:74
            return Move .LEFT #line:75
        elif O0OOO00O00O0O0000 .target [1 ]>O0OOO00O00O0O0000 .position [1 ]:#line:76
            return Move .UP #line:77
        else :#line:78
            return Move .DOWN #line:79
class Schumi :#line:82
    def __init__ (O00OO000000OOOO00 ):#line:84
        O00OO000000OOOO00 .previous_position =Move .STAY #line:85
        O00OO000000OOOO00 .grid_size =None #line:86
        O00OO000000OOOO00 .move_scores ={Move .UP :0 ,Move .LEFT :0 ,Move .DOWN :0 ,Move .RIGHT :0 }#line:87
        O00OO000000OOOO00 .move2direction ={Move .UP :[0 ,1 ],Move .LEFT :[-1 ,0 ],Move .DOWN :[0 ,-1 ],Move .RIGHT :[1 ,0 ]}#line:88
        O00OO000000OOOO00 .cross2 =[[0 ,2 ],[1 ,1 ],[2 ,0 ],[1 ,-1 ],[0 ,-2 ],[-1 ,-1 ],[-2 ,0 ],[-1 ,1 ]]#line:89
        O00OO000000OOOO00 .cross3 =[[0 ,3 ],[1 ,2 ],[-2 ,1 ],[-3 ,0 ],[-2 ,-1 ],[-1 ,-2 ],[0 ,-3 ],[1 ,-2 ],[2 ,-1 ],[3 ,0 ],[2 ,1 ],[1 ,2 ]]#line:90
    def get_name (O00000OOO00OOO000 ):#line:92
        return "Schumi"#line:93
    def get_contributor (OO00O0O0000O000O0 ):#line:95
        return "Ferdinand Schumacher"#line:96
    def reset_move_scores (O0O0O000OOO0OO00O ):#line:98
        for OO0OO0OO00OO0OOOO in O0O0O000OOO0OO00O .move_scores :#line:99
            O0O0O000OOO0OO00O .move_scores [OO0OO0OO00OO0OOOO ]=0 #line:100
    def get_cell (O00O0O0OO00OOOO00 ,OOOOO0OO0OOO0OOO0 ,OOOOO0O0O0OO0OOO0 ):#line:102
        return OOOOO0OO0OOO0OOO0 +OOOOO0O0O0OO0OOO0 #line:103
    def get_cell_score (O0000O000OOO0O0OO ,O0000OOOO00O0OO0O ,OO00OO000O0O0O00O ,OOOOO0OOOO0000OO0 ):#line:105
        if OO00OO000O0O0O00O [0 ]<0 or OO00OO000O0O0O00O [0 ]>O0000O000OOO0O0OO .grid_size -1 or OO00OO000O0O0O00O [1 ]<0 or OO00OO000O0O0O00O [1 ]>O0000O000OOO0O0OO .grid_size -1 :#line:107
            return -10 if OOOOO0OOOO0000OO0 else 0 #line:108
        elif np .array_equal (OO00OO000O0O0O00O ,O0000O000OOO0O0OO .previous_position ):#line:110
            return -1 #line:111
        else :#line:112
            OOO000O0OOOO0OOOO =O0000OOOO00O0OO0O [OO00OO000O0O0O00O [1 ],OO00OO000O0O0O00O [0 ]]#line:113
            if OOO000O0OOOO0OOOO ==0 :#line:114
                return 1 #line:115
            elif OOO000O0OOOO0OOOO ==O0000O000OOO0O0OO .id :#line:116
                return 0 #line:117
            else :#line:118
                return [-1 ,1 ,2 ][(O0000O000OOO0O0OO .id -OOO000O0OOOO0OOOO )%3 ]#line:120
    def update_move_scores (OO0O0O000OO00O0O0 ,O0O00O0O00O000OOO ,OO0OO0O0000OO0000 ):#line:122
        if O0O00O0O00O000OOO [0 ]<0 :#line:123
            OO0O0O000OO00O0O0 .move_scores [Move .LEFT ]+=OO0OO0O0000OO0000 #line:124
        if O0O00O0O00O000OOO [0 ]>0 :#line:125
            OO0O0O000OO00O0O0 .move_scores [Move .RIGHT ]+=OO0OO0O0000OO0000 #line:126
        if O0O00O0O00O000OOO [1 ]>0 :#line:127
            OO0O0O000OO00O0O0 .move_scores [Move .UP ]+=OO0OO0O0000OO0000 #line:128
        if O0O00O0O00O000OOO [1 ]>0 :#line:129
            OO0O0O000OO00O0O0 .move_scores [Move .DOWN ]+=OO0OO0O0000OO0000 #line:130
    def get_new_move (O0000O0000O000OOO ,OO00000O0OOOOOO00 ):#line:132
        O0000O0000O000OOO .reset_move_scores ()#line:133
        for O00O0O00000OO00O0 in O0000O0000O000OOO .move_scores :#line:135
            OOOOO0OOO0O0O0OO0 =O0000O0000O000OOO .get_cell (O0000O0000O000OOO .position ,O0000O0000O000OOO .move2direction [O00O0O00000OO00O0 ])#line:137
            O0000O0000O000OOO .move_scores [O00O0O00000OO00O0 ]=3.0 *O0000O0000O000OOO .get_cell_score (OO00000O0OOOOOO00 ,OOOOO0OOO0O0O0OO0 ,True )#line:139
        for O00OOOOO0OO00OOOO in O0000O0000O000OOO .cross2 :#line:141
            OOOOO0OOO0O0O0OO0 =O0000O0000O000OOO .get_cell (O0000O0000O000OOO .position ,O00OOOOO0OO00OOOO )#line:143
            O0000O0000O000OOO .update_move_scores (O00OOOOO0OO00OOOO ,1.0 *O0000O0000O000OOO .get_cell_score (OO00000O0OOOOOO00 ,OOOOO0OOO0O0O0OO0 ,False ))#line:145
        for O00OOOOO0OO00OOOO in O0000O0000O000OOO .cross3 :#line:147
            OOOOO0OOO0O0O0OO0 =O0000O0000O000OOO .get_cell (O0000O0000O000OOO .position ,O00OOOOO0OO00OOOO )#line:149
            O0000O0000O000OOO .update_move_scores (O00OOOOO0OO00OOOO ,0.5 *O0000O0000O000OOO .get_cell_score (OO00000O0OOOOOO00 ,OOOOO0OOO0O0O0OO0 ,False ))#line:151
        O000O0OO0OOO0000O =-10 #line:153
        OO0000000O0O0000O =Move .STAY #line:154
        O0OOO0OOO00OO0O00 =list (O0000O0000O000OOO .move_scores .keys ())#line:155
        random .shuffle (O0OOO0OOO00OO0O00 )#line:156
        for O00O0O00000OO00O0 in O0OOO0OOO00OO0O00 :#line:157
            OO00OO00OOOOOOO0O =O0000O0000O000OOO .move_scores [O00O0O00000OO00O0 ]#line:158
            if OO00OO00OOOOOOO0O >O000O0OO0OOO0000O :#line:159
                O000O0OO0OOO0000O =OO00OO00OOOOOOO0O #line:160
                OO0000000O0O0000O =O00O0O00000OO00O0 #line:161
        O0000O0000O000OOO .previous_position =O0000O0000O000OOO .position #line:163
        return OO0000000O0O0000O #line:164
    def determine_next_move (OOOOO00OOOOOOOO0O ,O00O00OOOOOO000O0 ,O0O000O000OOO0OO0 ,OOO0OO000O0O0O00O ):#line:166
        if OOOOO00OOOOOOOO0O .grid_size ==None :#line:168
            OOOOO00OOOOOOOO0O .grid_size =OOO0OO000O0O0O00O .grid_size #line:169
            OOOOO00OOOOOOOO0O .previous_position =OOOOO00OOOOOOOO0O .position #line:170
            return Move .STAY #line:171
        return OOOOO00OOOOOOOO0O .get_new_move (O00O00OOOOOO000O0 )