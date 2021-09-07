import ast
import astunparse

class NamingRefactor:
    def __init__(self):
        pass

    def search_ast(self, original_name, changed_name, constraints, dummy_constraints):
        tf = RefactorTransformer(original_name, changed_name, dummy_constraints)
        for module in constraints.values():
            for qt_dc in module.values():
                qt_dc._ast = tf.visit(qt_dc._ast)


class RefactorTransformer(ast.NodeTransformer):
    def __init__(self, original_name, changed_name, dummy_constraints):
        super(RefactorTransformer, self).__init__()
        self.original_name = original_name
        self.changed_name = changed_name
        # self.dummy_constraints = dummy_constraints

    def generic_visit(self, node):
        def search_info_dict(value):
            if type(value) == list:
                return [search_info_dict(list_element) for list_element in value]
            elif type(value) == str:
                tmp_ast = ast.parse(value)
                tmp_ast = self.visit(tmp_ast)
                return_code = astunparse.unparse(tmp_ast)[1:-1]     #delete first and last \n
                return return_code
            elif isinstance(value, ast.AST):
                tmp_ast = self.visit(value)
                return tmp_ast
            else:
                return value

        if 'name' in node.__dict__:
            node.name = self.changed_name if node.name == self.original_name else node.name
        elif 'info_dict' in node.__dict__:
            for key, value in node.info_dict.items():
                node.info_dict[key] = search_info_dict(value)
        elif type(node) == ast.Constant and type(node.value) == str:
            node = ast.Constant(node.value.replace(self.original_name,self.changed_name), None)

        return super(RefactorTransformer, self).generic_visit(node)


