dict = {
    '!!':'V',
    '@!':'F',
    '#!':'Y',
    '$!':'J',
    '%!':'6',
    '&!':'1',

    '!@':'5',
    '@@':'0',
    '#@':'M',
    '$@':'2',
    '%@':'9',
    '&@':'L',

    '!#':'I',
    '@#':'W',
    '##':'H',
    '$#':'S',
    '%#':'4',
    '&#':'Q',

    '!$':'K',
    '@$':'G',
    '#$':'B',
    '$$':'X',
    '%$':'T',
    '&$':'A',

    '!%':'E',
    '@%':'3',
    '#%':'C',
    '$%':'7',
    '%%':'P',
    '&%':'N',


    '!&':'U',
    '@&':'Z',
    '#&':'8',
    '$&':'R',
    '%&':'D',
    '&&':'O',
}

s = "&$ !# $# @%"

for i in s.split(' '):
    print(dict[i],end='')

print('{',end='')

s = "%$ #! $& %# &% &% @@ $# %# !& $& !& !@ _ $& @% $$ _ @$ !# !! @% _ #! @@ !& _ $# && #@ !% %$ ## !# &% @$ _ $& &$ &% %& && #@ _ !@ %$ %& %! $$ &# !# !! &% @% ## $% !% !& @! #& && %& !% %$ %# %$ @% ## %@ @@ $% ## !& #% %! %@ &@ %! &@ %$ $# ## %# !$ &% @% !% !& $& &% %# %@ #$ !# && !& #! %! ## #$ @! #% !! $! $& @& %% @@ && #& @% @! @# #@ @@ @& !@ %@ !# !# $# $! !@ &$ $@ !! @! &# @$ &! &# $! @@ &@ !% #% #! &@ &$ @@ &$ &! !& #! !# ## %$ !# !# %$ &! !# @# ## @@ $! $$ %# %$ @% @& $! &! !$ $# #$ $& #@ %@ @$ !% %& %! @% #% $! !! #$ &# ## &# && $& !! !% $! @& !% &@ !& $! @# !@ !& @$ $% #& #$ %@ %% %% &! $# !# $& #@ &! !# @! !@ @@ @@ ## !@ $@ !& $# %& %% !# !! $& !$ $% !! @$ @& !& &@ #$ && @% $& $& !% &! && &@ &% @$ &% &$ &@ $$"

for i in s.split(' '):
    try:
        print(dict[i],end='')
    except:
        print('_',end='')


print('}',end='')
