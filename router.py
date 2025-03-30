from operations.partition import partition_graph
from operations.spectral_drawing import spectral_drawing

operationMap = {
    "partition": partition_graph,
    "spectral_drawing": spectral_drawing
}

def process_request(data_process_request):
    data, data_process_operation = vars(data_process_request).values()
    options = data_process_operation.parameters
    operation = operationMap[data_process_operation.name]

    try:
        result = operation(*data.values(), *options.values())
    except:
        print("Data Operation Error")
        return {"error": "Data Operation Error"}
    else:
        return result
