def export(columns, results):
    result = {}
    allResults = []
    columns = [col.name for col in columns]

    if type(results) is list:
        for value in results:
            allResults.append(dict(zip(columns, value)))
        result['data'] = allResults
        return result

    elif type(results) is tuple:
        allResults.append(dict(zip(columns, results)))
        result['data'] = allResults
        return result
