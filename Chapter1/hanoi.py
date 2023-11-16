
from typing import TypeVar, Generic, List
T = TypeVar('T') #Variable introducida a partir de la version python 3.5 


class Stack(Generic[T]):

    def __init__(self) -> None: #constructor de la clase, define la lista con el nombre container de tipo List[T]
        self._container: List[T] = []

    #método que agrega "adjunta a la lista"
    def push(self, item: T) -> None: 
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

for i in range(1, num_discs + 1): #Carga los discos a la torre_a
    tower_a.push(i)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop()) #Primero saca del inicio (begin) y lo que saco lo pone en el fin (end)
        
    else:
        hanoi(begin, temp, end, n - 1) #Itera sin generar impacto hasta llegar a 1, cuando n llega a 1, hace la magia de end.push(begin.pop())
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)
