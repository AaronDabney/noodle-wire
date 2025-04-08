from operations.partition import partition_graph
from operations.spectral_drawing import spectral_drawing
from util.pydantic_models import Noodle_Request

operationMap = {
    "partition": partition_graph,
    "spectral_drawing": spectral_drawing
}

def process_request(request: Noodle_Request):
    graph = request.graph
    data_process_operation = request.metadata["data_process_operation"]
    options = data_process_operation["parameters"]
    operation = operationMap[data_process_operation["name"]]

    try:
        result = operation(graph, *options.values())
    except Exception as e:
        print(f"Data Operation Error: {str(e)}")
        return {"Error": f"Data Operation Error: {str(e)}"}
    else:
        return result
