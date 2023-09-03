from collections import Counter

def male_litery(lista):
    lowercase_list = list(map(str.lower, lista))
    return lowercase_list


def count_technologies(tech_list):
    tech_count = Counter(tech_list)
    return tech_count

def policz_posegreguj_technologie(lista_tech:list):
        # Użycie funkcji
    lista_tech2 = male_litery(lista_tech)
    result = count_technologies(lista_tech2)
    sorted_result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}

    lista_technologi = []

    final_dict = {}
    for tech, count in sorted_result.items():
        final_dict[tech] = count
    return final_dict


