import json


def ApplyPriceFilter(data: list[dict], minPrice: float, maxPrice: float) -> list[dict]:
    result = []
    for item in data:
        itemPrice = item["price"]
        if itemPrice < maxPrice and itemPrice >= minPrice:
            result.append(item)

    return result


def CheckRequiredFilters(genres: list[str], activeFilters: list[str]) -> bool:
    for activeFilter in activeFilters:
        if activeFilter not in genres:
            return False
    return True


def CheckNameParts(itemName: str, nameParts: list[str]) -> bool:
    for namePart in nameParts:
        if namePart.lower() not in itemName.lower():
            return False
    return True


def ApplyNameFileter(data: list[dict], nameParts: list[str]):
    result = []
    for item in data:
        if CheckNameParts(item["name"], nameParts):
            result.append(item)

    return result


def ApplyGenreFilter(data: list[dict], active_filters: list[str]):
    result = []
    for i in data:
        genres = i["genres"]
        if CheckRequiredFilters(genres, active_filters):
            result.append(i)

    return result

# def sort_json():
#     if 
