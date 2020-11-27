class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value



    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value


#Funkcja szukająca musi znalezc poszukiwany element, więc jedyną możliwą zwróconą wartością może być np. wartość True
#Jako, że przeszukujemy drzewo elementami, z ktorych je zbudowaliśmy, nie trzeba rozpatrywać co się stanie gdy takiego
#elementu nie odnajdziemy -> Głównie interesuje nas czas przeszukiwania takiego drzewa

    def find_val(self, looking_value):
        #Jesli szukana wartosc jest mniejsza od wartosci aktualnego wezla -> szukaj w lewym wezle wezla
        if looking_value < self.value:
            return self.left.find_val(looking_value)
        elif looking_value > self.value:
            return self.right.find_val(looking_value)
        else:
            return True
        #return False


    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value)
        if self.right:
            self.right.printTree()


def maximumValue(root):
     
    while root.right:
        root = root.right
 
    return root


def deleteNode(root, deleted_value):
     
    # Gdy szukana wartosc nie znajduje sie w drzewie
    if root is None:
        return root
 
    # Tutaj czesc odpowiedzialna za przeszukiwanie drzewa 
    if deleted_value < root.value:
        root.left = deleteNode(root.left, deleted_value)
 
    # To samo
    elif deleted_value > root.value:
        root.right = deleteNode(root.right, deleted_value)
 
    # A gdy znajdziemy szukaną wartość
    else:
 
        # Brak potomkow
        if root.left is None and root.right is None:
            return None
 
        #  Ma dwoje potomkow, szukamy najwiekszej wartosci z lewego drzewa do podmianki
        elif root.left and root.right:
            
            temp = maximumValue(root.left)
 
            root.value = temp.value

            # Usuniecie tej wartosci (jej dublera)
            root.left = deleteNode(root.left, temp.value)
 
        # Wezel ma jednego potomka
        else:

            child = root.left if root.left else root.right
            root = child
 
    return root





