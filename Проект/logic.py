class Combination:
    def __init__(self, ferum : tuple, hard: tuple) -> None:
        self.ferum_begin = ferum[0]
        self.ferum_end = ferum[1]
        self.hard_begin = hard[0]
        self.hart_end = hard[1]

class Logic:
    ABS_MAX = 100

    FERUM_HARD_COMBINES = [
    Combination((0, 3), (0, 0.3)), 
    Combination((0, 3), (0.3, 0.9)), 
    Combination((0, 3), (0.9, 8)),
    Combination((3, 8), (0, 0.3)),
    Combination((3, 8), (0.3, 8)),
    Combination((8, 15), (0, 0.3)),
    Combination((8, 15), (0.3, 8)),
    Combination((8, 15),(8, ABS_MAX)),
    Combination((15, ABS_MAX),(8, ABS_MAX))
    ]

    HOUSE_BASE_LOGIC_DICT = {
        
        FERUM_HARD_COMBINES[0]: [
            
                    #ВВ0020 - BB20 (Карбон-блок)
                    #ВВ0021 - BB20 (Феронить)
                    #ES0000 - Expert Standart 
                    #PR0111 - Профи Осмо
                    #WF0111 - Барьер Waterfort
                    #ЕC0000 - Expert Complex
                    #EX0000 - Expert смягчение
                    #KL1044 - Колонна 1044
                    #KL1252 - Колонна 1252
                    #KL1354 - Колонна 1354
                    #KL1465 - Колонна 1465
                    #BU0034 - Блок управления 100v3/4
                    #BU1001 - Блок управления 100V1 
                    #EM0025 - Ecomix A (25л)
                    #EM0050 - Ecomix A (50л)
                    #EM0060 - Ecomix A (62,5л)
                    #EM0800 - Ecomix A (80л)
                    #EM0052 - Ecomix P (50л)
                    #EM0062 - Ecomix P (62,5л) 
                    #EM0080 - Ecomix P (80л)
                    #EM0051 - Ecomix C (50л)
                    #EM0063 - Ecomix C (62,5л)
                    #EM0081 - Ecomix C (80л)
                    #SM0025 - Softmix (25л)
                    #SM0050 - Softmix (50л)
                    #SM0062 - Softmix (62,5л)
                    #SM0080 - Softmix (80л)
                    #FM0050 - Ferromix (50)
                    #FM0062 - Ferromix (62,5)
                    #FM0080 - Ferromix (80)
                    #ВA0100 - Колонна аэрации Barier Aero Pro 100
                    #KG0050 - 50 кг соли
                    #SB0000 - Солевой бак
                                  
                    
                    {'main_filters_components': ['BB0020'], 'kitchen_filters': ['ES0000', 'PR0111', 'WF0111']},
                    {'main_filters_components': ['BB0020'], 'kitchen_filters': ['ES0000', 'PR0111', 'WF0111']},
                    {'main_filters_components': ['BB0020'], 'kitchen_filters': ['ES0000', 'PR0111', 'WF0111']},
                    {'main_filters_components': ['BB0020'], 'kitchen_filters': ['ES0000', 'PR0111', 'WF0111']}
                    ],
        FERUM_HARD_COMBINES[1]: [
                    {'main_filters_components': ['BB0021'], 'kitchen_filters': ['EС0000', 'PR0111', 'WF0111']},
                    {'main_filters_components': ['KL1044', 'BU0034', 'EM0025', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EС0000',  'PR0111', 'WF0111']},
                    {'main_filters_components': ['KL1354', 'BU1001', 'EM0062', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EС0000', 'PR0111', 'WF0111']},
                    {'main_filters_components': ['KL1465', 'BU1001', 'EM0080', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EС0000', 'PR0111', 'WF0111']}
                    ],
        FERUM_HARD_COMBINES[2]: [
                    {'main_filters_components': ['KL1044', 'BU0034', 'EM0025', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EС0000', 'PR0111', 'WF0111']},
                    {'main_filters_components': ['KL1252', 'BU1001', 'EM0050', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EС0000',  'PR0111', 'WF0111']},
                    {'main_filters_components': ['KL1354', 'BU1001', 'EM0063', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EС0000', 'PR0111', 'WF0111']},
                    {'main_filters_components': ['KL1465', 'BU1001', 'EM0081', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EС0000', 'PR0111', 'WF0111']}
                    ],
        FERUM_HARD_COMBINES[3]: [
                    {'main_filters_components': ['KL1044', 'BU0034', 'SM0025', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EX0000', 'PR0111', 'WF0111']},
                    {'main_filters_components': ['KL1252', 'BU1001', 'SM0050', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EX0000', 'PR0111', 'WF0111']},
                    {'main_filters_components': ['KL1354', 'BU1001', 'SM0062', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EX0000', 'PR0111', 'WF0111']},
                    {'main_filters_components': ['KL1465', 'BU1001', 'SM0080', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EX0000', 'PR0111', 'WF0111']}
                    ],
        FERUM_HARD_COMBINES[4]: [
                    {'main_filters_components': ['KL1044', 'BU0034', 'EM0025', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EС0000', 'PR0111', 'WF0111']},
                    {'main_filters_components': ['KL1252', 'BU1001', 'EM0050', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EX0000',  'PR0111', 'WF0111']},
                    {'main_filters_components': ['KL1354', 'BU1001', 'EM0060', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EС0000', 'PR0111', 'WF0111']},
                    {'main_filters_components': ['KL1465', 'BU1001', 'EM0800', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EС0000', 'PR0111', 'WF0111']}
                    ],
        FERUM_HARD_COMBINES[5]: [
                    {'main_filters_components': ['KL1252', 'BU1001', 'SM0050', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EX0000', 'PR0111', 'WF0111'], 'kitchen_filters': ['KF0021']},
                    {'main_filters_components': ['KL1252', 'BU1001', 'SM0050', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EX0000', 'PR0111', 'WF0111'], 'kitchen_filters': ['KF0021']},
                    {'main_filters_components': [''], 'kitchen_filters': ['']},
                    {'main_filters_components': [''], 'kitchen_filters': ['']}
                    ],
        FERUM_HARD_COMBINES[6]: [
                    {'main_filters_components': ['KL1252', 'BU1001', 'EM0050', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EС0000', 'PR0111', 'WF0111']},
                    {'main_filters_components': ['KL1252', 'BU1001', 'EM0051', 'KG0050', 'SB0000', 'ВВ0020', 'KL1354', 'BU1001', 'EM0060', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['EС0000', 'PR0111', 'WF0111']},
                    {'main_filters_components': ['KL1354', 'BU1001', 'EM0060', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['']},
                    {'main_filters_components': ['KL1465', 'BU1001', 'EM0800', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['']}
                    ],
        FERUM_HARD_COMBINES[7]: [
                    {'main_filters_components': ['ВA0100', 'KL1252', 'FM0050', 'KL1252', 'EM0052', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['']},
                    {'main_filters_components': ['ВA0100', 'KL1354', 'FM0062', 'KL1354', 'EM0062', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['']},
                    {'main_filters_components': ['ВA0100', 'KL1354', 'FM0062', 'KL1354', 'EM0062', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['']},
                    {'main_filters_components': ['ВA0100', 'KL1465', 'FM0080', 'KL1465', 'EM0080', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['']}
                    ],
        FERUM_HARD_COMBINES[8]: [
                    {'main_filters_components': ['ВA0100', 'KL1252', 'FM0050', 'KL1252', 'EM0051', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['']},
                    {'main_filters_components': ['ВA0100', 'KL1354', 'FM0062', 'KL1354', 'EM0062', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['']},
                    {'main_filters_components': ['ВA0100', 'KL1354', 'FM0062', 'KL1354', 'EM0062', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['']},
                    {'main_filters_components': ['ВA0100', 'KL1465', 'FM0080', 'KL1465', 'EM0080', 'KG0050', 'SB0000', 'ВВ0020'], 'kitchen_filters': ['']}
                    ],
    }

    def __get_dict_index(self, people_num):
        
        if people_num < 3:
            return 0
        if people_num < 5:
            return 1
        if people_num < 8:
            return 2
        return 3

    def get_id_lists(self, water_ferum, water_hard, people_num,):
        for comb in self.FERUM_HARD_COMBINES:
            if (water_ferum >= comb.ferum_begin and water_ferum <= comb.ferum_end) \
                and (water_hard >= comb.hard_begin and water_ferum < comb.hart_end):
                
                return self.HOUSE_BASE_LOGIC_DICT[self.__get_dict_index(people_num)]

