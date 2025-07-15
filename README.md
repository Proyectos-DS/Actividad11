# Actividad 11 - Escribir aserciones en pruebas con pytest

### Estructura final de la Actividad

├── src
│   ├── __init__.py
│   └── stack.py
├── tests
│   ├── __init__.py
│   └── test_stack.py
├── Instrucciones.md
├── README.md
├── requirements.txt
└── setup.cfg


## Paso 1: Instalación de pytest y pytest-cov

Instalación de `pytest` y `pytest-cov`:

Cree un archivo `requirements.txt` con los modulos `pytest` y `pytest-cov`. Luego ejecute el comando:


```sh
pip install -r requirements.txt
```

**La instalación fue exitosa**

## Paso 2: Archivos de prueba.

Esta fue mi implementación de `stack.py`:

```python
from typing import Any


class Stack:

    def _init__(self):
        self.stack: list[Any] = []
        self.size = 0

    def push(self, data: Any) -> None:
        self.stack.insert(0, data)
        self.size += 1

    def pop(self) -> Any:
        if self.size > 1:
            self.stack.pop(0)
            self.size -= 1

    def peek(self) -> Any:
        data = self.stack[0]
        return data

    def is_empty(self) -> bool:
        return self.size == 0
```

Para este paso no escribí funciones de prueba, lo dejaré para los siguientes pasos.


## Paso 3: Escribiendo aserciones para el método `is_empty()`.
En la guía usan metodos con unittest, pero esta al ser una actividad de pytest modifique el código. El código que implementé para las pruebas fue este:

```python
import pytest
from src.stack import Stack

def test_is_empty():
    stack = Stack()
    size = stack.size
    assert stack.is_empty() == True, f"La pila tiene {size} elementos"  # La pila recién creada debe estar vacía
    stack.push(5)
    assert stack.is_empty() == False  # Después de agregar un elemento, la pila no debe estar vacía


def test_pop():
    stack = Stack()
    stack.push(3)
    stack.push(5)
    assert stack.pop() == 5
    assert stack.peek() == 3
    stack.pop()
    assert stack.is_empty() == True
```

## Paso 4.
Las pruebas se ejecutaron con exito:

```sh
(.venv) dirac@ubuntu:~/Documents/DS/Actividad11$ pytest -v
============================================== test session starts ===============================================
platform linux -- Python 3.12.3, pytest-8.4.1, pluggy-1.6.0 -- /home/dirac/Documents/DS/Actividad11/.venv/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/dirac/Documents/DS/Actividad11
plugins: cov-6.2.1
collected 2 items                                                                                                

test_stack.py::test_is_empty PASSED                                                                        [ 50%]
test_stack.py::test_pop PASSED                                                                             [100%]

=============================================== 2 passed in 0.02s ================================================
(.venv) dirac@ubuntu:~/Documents/DS/Actividad11$ 
```

## Paso 5: Escribiendo aserciones para el método `peek()`

Se agrego la prueba para `peek()`:

```python
def test_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2  # El valor superior debe ser el último agregado (2)
    assert stack.peek() == 2  # La pila no debe cambiar después de peek()
```

Las pruebas fueron exitosas:

```sh
test_stack.py::test_is_empty PASSED                                                                        [ 33%]
test_stack.py::test_pop PASSED                                                                             [ 66%]
test_stack.py::test_peek PASSED                                                                            [100%]

=============================================== 3 passed in 0.06s ================================================
(.venv) dirac@ubuntu:~/Documents/DS/Actividad11$ 
```

## Paso 6: Escribiendo asercioens para el método `pop()`

Viendo mejor la guía, incluye pruebas con **unittest** para cada método así que creo que usarlas forma parte crucial de la actividad. Aqui se presenta la inclusión de esas pruebas en el archivo `test_stack.py`

```python
class TestStack(TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_pop(self):
        self.stack.push(3)
        self.stack.push(5)
        self.assertEqual(self.stack.pop(), 5)
        self.assertEqual(self.stack.peek(), 3)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_peek(self):
        self.stack.push(3)
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)

    def test_pop(self):
        self.stack.push(3)
        self.stack.push(5)
        self.assertEqual(self.stack.pop(), 5)
        self.assertEqual(self.stack.peek(), 3)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())
```

Los pruebas fueron exitosas:

```sh
(.venv) dirac@ubuntu:~/Documents/DS/Actividad11$ pytest -v
============================================== test session starts ===============================================
platform linux -- Python 3.12.3, pytest-8.4.1, pluggy-1.6.0 -- /home/dirac/Documents/DS/Actividad11/.venv/bin/python3.12
cachedir: .pytest_cache
rootdir: /home/dirac/Documents/DS/Actividad11
plugins: cov-6.2.1
collected 5 items                                                                                                

test_stack.py::TestStack::test_peek PASSED                                                                 [ 20%]
test_stack.py::TestStack::test_pop PASSED                                                                  [ 40%]
test_stack.py::test_is_empty PASSED                                                                        [ 60%]
test_stack.py::test_pop PASSED                                                                             [ 80%]
test_stack.py::test_peek PASSED                                                                            [100%]

=============================================== 5 passed in 0.09s ================================================
(.venv) dirac@ubuntu:~/Documents/DS/Actividad11$ 
```


## Paso 7: Escribiendo asercioens para el método `push()`

Las pruebas también se ejecutaron con exito. El proceso es el mismo, asi que solo presentaré los resultados:

```sh
test_stack.py::TestStack::test_peek PASSED                                                                 [ 14%]
test_stack.py::TestStack::test_pop PASSED                                                                  [ 28%]
test_stack.py::TestStack::test_push PASSED                                                                 [ 42%]
test_stack.py::test_is_empty PASSED                                                                        [ 57%]
test_stack.py::test_pop PASSED                                                                             [ 71%]
test_stack.py::test_peek PASSED                                                                            [ 85%]
test_stack.py::test_push PASSED                                                                            [100%]

=============================================== 7 passed in 0.08s ================================================
(.venv) dirac@ubuntu:~/Documents/DS/Actividad11$ 
```



## Paso 8: Ejecuta pytest para verificar todas las pruebas.

**Redundante**, se puede ver en el paso 7 que se ejecutaron las pruebas.



## Paso 9 Agregando  cobertura de pruebas con pytest-cov

Se puede ver que las pruebas estaán cubiertas al 100%:

```sh
(.venv) dirac@ubuntu:~/Documents/DS/Actividad11$ pytest --cov=src --cov-report term-missing
============================================== test session starts ===============================================
platform linux -- Python 3.12.3, pytest-8.4.1, pluggy-1.6.0
rootdir: /home/dirac/Documents/DS/Actividad11
plugins: cov-6.2.1
collected 7 items                                                                                                

tests/test_stack.py .......                                                                                [100%]

================================================= tests coverage =================================================
________________________________ coverage: platform linux, python 3.12.3-final-0 _________________________________

Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
src/__init__.py       0      0   100%
src/stack.py         16      0   100%
-----------------------------------------------
TOTAL                16      0   100%
=============================================== 7 passed in 0.34s ================================================
(.venv) dirac@ubuntu:~/Documents/DS/Actividad11$ 
```
