# -*- coding: utf-8 -*-
# tab = t | character = c | attr = a |  = e | skill = s
# tab group
table = {
    'group': '-tab-group-',
    'character': '-tab-character-',
    'attr': '-tab-attr-',
    'skill': '-tab-skill-',
    'eqpt': '-tab-eqpt-',
    'json': '-tab-json-'

}


# character
character = {
    'list': '-character-list-box-',
    'text': {
        'id': '-character-id-text',
        'name': '-character-name-text-',
        'nickname': '-character-nickname-text-',
        'cv': '-character-cv-text-',
        'sex': '-character-sex-text-',

        'intro': '-character-intro-text-'
    },
    'relate': {
        '-character-id-': 'id',
        '-character-name-': 'name',
        '-character-nickname-': 'nickname',
        '-character-cv-': 'cv',
        '-character-sex-male-': 'sex',
        '-character-sex-female-': 'sex',
        '-character-intro-': 'intro'
    },
    'data': {
        'id': '-character-id-',
        'name': '-character-name-',
        'nickname': '-character-nickname-',
        'cv': '-character-cv-',
        'male': '-character-sex-male-',
        'female': '-character-sex-female-',
        'intro': '-character-intro-'
    },
    'button': {
        'save': '-character-button-save-',
        'new': '--character-button-new-',
        'clear': '-character-button-clear-'
    }
}

skill = {
    'list': '-skill-list-box-',
    'children': {
        'list': '-skill-children-list-box-',
        'choose': '-skill-children-choose-'
    },
    'text': {
        'id': '-skill-id-text',
        'name': '-skill-name-text-',
        'buff': '-skill-buff-text-',
        'debuff': '-skill-debuff-text-',
        'use': '-skill-use-text-',
        'time': '-skill-time-text-',
        'kind': '-skill-kind-text-',
        'access': '-skill-access-text-',

        'hp': '-skill-hp-text-',
        'mp': '-skill-mp-text-',
        'str': '-skill-str-text-',
        'vit': '-skill-vit-text-',
        'agi': '-skill-agi-text-',
        'dex': '-skill-dex-text-',
        'int': '-skill-int-text-',

        'hp_p': '-skill-hp-point-text- ',
        'mp_p': '-skill-mp-point-text- ',
        'str_p': '-skill-str-point-text- ',
        'vit_p': '-skill-vit-point-text- ',
        'agi_p': '-skill-agi-point-text- ',
        'dex_p': '-skill-dex-point-text- ',
        'int_p': '-skill-int-point-text- '
    },
    'relate': {
        '-skill-id-': 'id',
        '-skill-name-': 'name',
        '-skill-buff-': 'buff',
        '-skill-debuff-': 'debuff',
        '-skill-use-': 'use',
        '-skill-time-': 'time',
        '-skill-active-': 'kind',
        '-skill-passive-': 'kind',
        '-skill-trigger-': 'kind',
        '-skill-access-': 'access',

        '-skill-hp-': 'hp',
        '-skill-mp-': 'mp',
        '-skill-str-': 'str',
        '-skill-vit-': 'vit',
        '-skill-agi-': 'agi',
        '-skill-dex-': 'dex',
        '-skill-int-': 'int',

        '-skill-hp-point- ': 'hp_p',
        '-skill-mp-point- ': 'mp_p',
        '-skill-str-point- ': 'str_p',
        '-skill-vit-point- ': 'vit_p',
        '-skill-agi-point- ': 'agi_p',
        '-skill-dex-point- ': 'dex_p',
        '-skill-int-point- ': 'int_p'

    },
    'data': {
        'id': '-skill-id-',
        'name': '-skill-name-',
        'buff': '-skill-buff-',
        'debuff': '-skill-debuff-',
        'use': '-skill-use-',
        'time': '-skill-time-',
        'active': '-skill-active-',
        'passive': '-skill-passive-',
        'trigger': '-skill-trigger-',
        'access': '-skill-access-',

        'hp': '-skill-hp-',
        'mp': '-skill-mp-',
        'str': '-skill-str-',
        'vit': '-skill-vit-',
        'agi': '-skill-agi-',
        'dex': '-skill-dex-',
        'int': '-skill-int-',

        'hp_p': '-skill-hp-point-',
        'mp_p': '-skill-mp-point-',
        'str_p': '-skill-str-point-',
        'vit_p': '-skill-vit-point-',
        'agi_p': '-skill-agi-point-',
        'dex_p': '-skill-dex-point-',
        'int_p': '-skill-int-point-'
    },
    'button': {
        'save': '-skill-button-save-',
        'new': '-skill-button-new-',
        'clear': '-skill-button-clear-'
    }
}

eqpt = {
    'list': '-eqpt-list-box-',
    'skill': {
        'list': '-eqpt-skill-list-box-',
        'choose': '-eqpt-skill-choose-'
    },
    'slot': {
        'list': '-eqpt-slot-list-box-',
        'choose': '-eqpt-slot-choose-'
    },
    'text': {
        'id': '-eqpt-id-text-',
        'name': '-eqpt-name-text',
        'access': '-eqpt-access-text-',

        'hp': '-eqpt-hp-text-',
        'mp': '-eqpt-mp-text-',
        'str': '-eqpt-str-text-',
        'vit': '-eqpt-vit-text-',
        'agi': '-eqpt-agi-text-',
        'dex': '-eqpt-dex-text-',
        'int': '-eqpt-int-text-',

        'hp_p': '-eqpt-hp-point-text- ',
        'mp_p': '-eqpt-mp-point-text- ',
        'str_p': '-eqpt-str-point-text- ',
        'vit_p': '-eqpt-vit-point-text- ',
        'agi_p': '-eqpt-agi-point-text- ',
        'dex_p': '-eqpt-dex-point-text- ',
        'int_p': '-eqpt-int-point-text- '

    },
    'data': {
        'id': '-eqpt-id-',
        'name': '-eqpt-name-',
        'access': '-eqpt-access-',

        'hp': '-eqpt-hp-',
        'mp': '-eqpt-mp-',
        'str': '-eqpt-str-',
        'vit': '-eqpt-vit-',
        'agi': '-eqpt-agi-',
        'dex': '-eqpt-dex-',
        'int': '-eqpt-int-',

        'hp_p': '-eqpt-hp-point-',
        'mp_p': '-eqpt-mp-point-',
        'str_p': '-eqpt-str-point-',
        'vit_p': '-eqpt-vit-point-',
        'agi_p': '-eqpt-agi-point-',
        'dex_p': '-eqpt-dex-point-',
        'int_p': '-eqpt-int-point-'

    },
    'relate': {
        '-eqpt-id-': 'id',
        '-eqpt-name-': 'name',
        '-eqpt-access-': 'access',

        '-eqpt-hp-': 'hp',
        '-eqpt-mp-': 'mp',
        '-eqpt-str-': 'str',
        '-eqpt-vit-': 'vit',
        '-eqpt-agi-': 'agi',
        '-eqpt-dex-': 'dex',
        '-eqpt-int-': 'int',

        '-eqpt-hp-point- ': 'hp_p',
        '-eqpt-mp-point- ': 'mp_p',
        '-eqpt-str-point- ': 'str_p',
        '-eqpt-vit-point- ': 'vit_p',
        '-eqpt-agi-point- ': 'agi_p',
        '-eqpt-dex-point- ': 'dex_p',
        '-eqpt-int-point- ': 'int_p'

    },
    'button': {
        'save': '-eqpt-button-save-',
        'new': '-eqpt-button-new-',
        'clear': '-eqpt-button-clear-'
    }
}

attr = {
    'list': '-attr-list-box-',
    'skill': {
        'list': '-attr-skill-list-box-',
        'choose': '-attr-skill-choose-'
    },
    'text': {
        'id': '-attr-id-text-',
        'time': '-attr-time-text',
        'time_a': '-attr-time-a-text',
        'code': '-attr-code-text-',
        'level': '-attr-level-text-',

        'hp': '-attr-hp-text-',
        'mp': '-attr-mp-text-',
        'str': '-attr-str-text-',
        'vit': '-attr-vit-text-',
        'agi': '-attr-agi-text-',
        'dex': '-attr-dex-text-',
        'int': '-attr-int-text-',

        'head': '-attr-head-text-',
        'body': '-attr-body-text-',
        'r_hand': '-attr-r-hand-text-',
        'l_hand': '-attr-l-hand-text-',
        'log': '-attr-log-text-',
        'foot': '-attr-foot-text-',
        'jew1': '-attr-jew1-text-',
        'jew2': '-attr-jew2-text-',
        'jew3': '-attr-jew3-text-'
    },
    'data': {
        'id': '-attr-id-',
        'time': '-attr-time-',
        'time_a': '-attr-time-a-',
        'code': '-attr-code-',
        'level': '-attr-level-',

        'hp': '-attr-hp-',
        'mp': '-attr-mp-',
        'str': '-attr-str-',
        'vit': '-attr-vit-',
        'agi': '-attr-agi-',
        'dex': '-attr-dex-',
        'int': '-attr-int-',

        'head': '-attr-head-',
        'body': '-attr-body-',
        'r_hand': '-attr-r-hand-',
        'l_hand': '-attr-l-hand-',
        'log': '-attr-log-',
        'foot': '-attr-foot-',
        'jew1': '-attr-jew1-',
        'jew2': '-attr-jew2-',
        'jew3': '-attr-jew3-'
    },
    'relate': {
        '-attr-id-': 'id',
        '-attr-time-': 'time',
        '-attr-time-a-': 'time_a',
        '-attr-code-': 'code',
        '-attr-level-': 'level',

        '-attr-hp-': 'hp',
        '-attr-mp-': 'mp',
        '-attr-str-': 'str',
        '-attr-vit-': 'vit',
        '-attr-agi-': 'agi',
        '-attr-dex-': 'dex',
        '-attr-int-': 'int',

        '-attr-head-': 'head',
        '-attr-body-': 'body',
        '-attr-r-hand-': 'r_hand',
        '-attr-l-hand-': 'l_hand',
        '-attr-log-': 'log',
        '-attr-foot-': 'foot',
        '-attr-jew1-': 'jew1',
        '-attr-jew2-': 'jew2',
        '-attr-jew3-': 'jew3'
    },
    'button': {
        'save': '-attr-button-save-',
        'new': '-attr-button-new-',
        'clear': '-attr-button-clear-'
    }
}

json = {
    'text': '-json-text-',
    'button': '-json-button-'
}