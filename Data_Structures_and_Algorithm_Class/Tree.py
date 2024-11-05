# 연산자 여부 판단
def isOperator(op) -> bool:
    return op == '+' or op == '-' or op == '*' or op == '/'

# 클래스 설계: LinkedBTree
class LinkedBTree:
    class DNode:
        def __init__ (self, data, Llink=None, Rlink=None):
            self.data = data
            self.Llink = Llink
            self.Rlink = Rlink

    def __init__(self):
        self.__root = None

    # 이진 트리(수식 트리) 생성: 스택 구조 활용
    def makeLinkedBTree(self, postfix) -> 'DNode':  
        postfix = postfix.split()
        s = []
        for ch in postfix:
            tNode = self.DNode(ch) 
            if isOperator(ch):
                tNode.Rlink = s.pop()
                tNode.Llink = s.pop()
            s.append(tNode)
        self.__root = s.pop()
        return self.__root

    # 깊이 우선 순회: 전위, 중위, 후위 순회
    def Preorder(self) -> None:
        def __Preorder(tNode):
            if tNode:
                print(tNode.data, end=' ')
                __Preorder(tNode.Llink)
                __Preorder(tNode.Rlink)
        __Preorder(self.__root)  

    def Inorder(self) -> None:
        def __Inorder(tNode):
            if tNode:
                __Inorder(tNode.Llink)
                print(tNode.data, end=' ')
                __Inorder(tNode.Rlink)
        __Inorder(self.__root)  

    def Postorder(self) -> None:
        def __Postorder(tNode):
            if tNode:
                __Postorder(tNode.Llink)
                __Postorder(tNode.Rlink)
                print(tNode.data, end=' ')
        __Postorder(self.__root)  
        
    # 너비 우선 순회
    def Levelorder(self) -> None:
        if not self.__root:
            return
        q = [self.__root]
        while q:
            tNode = q.pop(0)
            print(f'{tNode.data}', end=' ')
            if tNode.Llink:
                q.append(tNode.Llink)
            if tNode.Rlink:
                q.append(tNode.Rlink)

    def __del__(self):
        if not self.__root:
            return
        q = [self.__root]
        while q:
            tNode = q.pop(0)
            if tNode.Llink:
                q.append(tNode.Llink)
            if tNode.Rlink:
                q.append(tNode.Rlink)
            del tNode

if __name__ == '__main__':
    postfix = input('트리를 구성할 후위 수식: ')
    BTree = LinkedBTree()
    BTree.makeLinkedBTree(postfix)

    # 깊이 우선 순회: 전위, 중위, 후위 순회
    print('Preorder  : ', end=' ')
    BTree.Preorder()
    print('')
    print('Inorder   : ', end=' ')
    BTree.Inorder()
    print('')
    print('Postorder : ', end=' ')
    BTree.Postorder()
    print('')

    # 너비 우선 순회
    print('Levelorder: ', end=' ')
    BTree.Levelorder()
    print('')
