
class Interpreter:

    def __init__(self) -> None:
        pass

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = self.__getattribute__(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f"No visit_{type(node).__name__} method found for this node")

    def visit_NumberNOde(self, node):
        print("Found number node")

    def visit_BinaryOperationNode(self, node)