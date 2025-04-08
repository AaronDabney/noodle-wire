from typing import Dict
from typing import Optional
from pydantic import BaseModel

class Edge_MetaData(BaseModel):
    weight: int

    class Config:
        extra = "allow"

class Node_Metadata(BaseModel):
    class Config:
        extra = "allow"

class Data_Process_Operation(BaseModel):
    name: str
    parameters: dict

class Graph_Metadata(BaseModel):
    data_process_operation: Data_Process_Operation
    notes: str | None

    class Config:
        extra = "allow"

class Node(BaseModel):
    label: str
    metadata: Optional[Node_Metadata] = None

class Edge(BaseModel):
    source: str
    target: str
    metadata: Edge_MetaData

class Graph(BaseModel):
    directed: bool | None # string?
    label: str
    nodes: Dict[str, Node] | None
    edges: list[Edge] = []

class Noodle_Request(BaseModel):
    graph: Graph
    metadata: dict
