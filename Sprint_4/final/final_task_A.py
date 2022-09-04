# 69495747

"""
-- ПРИНЦИП РАБОТЫ --
Я решил, что реализацию поисковой системы нужно разбыть на 2 этапа:
1. Построение индексов.
    Идексы решил построить по структуре
    {
        word: {document_id: count_words_in_documents}
    }
    для лучше поиска соответсвий в дальнейшем.

2. Поиск соответствий в запросе на основе индексов.
    Пробегаясь по запросу ищу проиндексированные слова, беру их
    количества вхождений в разные документы и записываю в результат поиска по запросу.

    Таким образом, когда я переберу все слова,
    то у меня будет словарь с количествами вхождений в разных документах.

    Далее сортирую полученный результат и вывожу первые пять релевантных документов.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
n - количество документов
m - количество запросов

Построение индексов - О(n^2).
Поиск совпадений в запросах - О(m).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Для построения поискового индекса требуется О(n) памяти.
"""


def search_in_query(query: str, indexes: dict) -> str:
    res = {}
    for index in set(query.split(' ')):
        if indexes.get(index):
            for file_id in indexes[index]:
                value = indexes[index][file_id]
                if res.get(file_id):
                    res[file_id] -= value
                else:
                    res[file_id] = -value

    res = [(res[file_id], file_id) for file_id in res]
    result = [file_id for weight, file_id in sorted(res)][:5]
    return " ".join(str(i) for i in result)


def create_index(indexes, id, doc):
    for index in doc.split(' '):
        if indexes.get(index):
            indexes[index][id] = indexes[index].get(id, 0) + 1 
        else:
            indexes[index] = {id: 1}


if __name__ == '__main__':
    cnt_docs = int(input())
    indexes = {}
    for id in range(1, cnt_docs+1):
        create_index(indexes, id, input())

    cnt_query = int(input())
    for _ in range(cnt_query):
        print(search_in_query(input(), indexes))
